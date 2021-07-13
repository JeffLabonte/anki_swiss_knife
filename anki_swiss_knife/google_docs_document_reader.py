import re
import os
from pathlib import Path
from typing import List

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

from anki_swiss_knife.helper import files
from anki_swiss_knife.constants import file_paths

DATE_REGEX = re.compile(r"[0-9]{3}")


class GoogleDocsDocumentReader:
    """
    Extracts a Google Doc document into a .txt file. That .txt file can
    be parsed into a CSV file. The CSV file is to be imported by Anki afterwards
    """

    SCOPES = [
        "https://www.googleapis.com/auth/documents",
    ]

    VOCAB_START_FLAG = "END FIRST PAGE"

    _GDOCS_PARAGRAPH = "paragraph"
    _GDOCS_ELEMENTS = "elements"
    _GDOCS_TABLE = "table"
    _GDOCS_TABLE_ROWS = "tableRows"
    _GDOCS_TABLE_CELLS = "tableCells"
    _GDOCS_TABLE_OF_CONTENTS = "tableOfContents"

    def __init__(
        self,
        output_folder: str,
    ):
        """
        output_folder is expected to use this format:

        /home/username/path/to/store/stuff/in/
        """
        self._credentials = None
        self.service = None
        self.output_folder = output_folder
        self.init()

    def init(self):
        self._login_to_google()
        files.create_folder(file_path=self.output_folder)

    def get_document(self, document_id: str):
        return self.service.documents().get(documentId=document_id)

    def _login_to_google(self):
        filepath = Path(
            Path.joinpath(
                Path.home(),
                ".config",
                "anki_swiss_tool",
                "credentials.json",
            )
        )
        if filepath.exists():
            self._credentials = Credentials.from_service_account_file(filename=filepath, scopes=self.SCOPES)
            self.service = build("docs", "v1", credentials=self._credentials)
        else:
            raise FileNotFoundError()

    def is_valid_text(self, element):
        return element and DATE_REGEX.match(element) is None

    def find_page_flag(self, contents: List[str]) -> int:
        for index, content in enumerate(contents):
            if self.VOCAB_START_FLAG in content:
                return index

    def extract_document_to_file(self, document_id: str) -> Path:
        """
        Extract document from Google Docs into a .txt file
        so it can be processed for Anki as CSV.
        """
        document = self.get_document(document_id=document_id).execute()
        document_contents = document["body"]["content"]

        text_contents = self.read_structural_element(elements=document_contents)
        contents = [f"{content}\n" for content in text_contents.split("\n") if self.is_valid_text(element=content)]
        vocabulary_start_index = self.find_page_flag(contents=contents)
        saved_file_path = os.path.join(self.output_folder, f"{document['title']}.txt")
        with open(saved_file_path, "w+") as f:
            f.writelines(contents[vocabulary_start_index + 1 :])
            print(f"[+] File saved: {saved_file_path}")
            return saved_file_path

    def read_paragraph_element(self, element):
        text_run = element.get("textRun")
        if not text_run:
            return ""
        return text_run.get("content")

    def read_structural_element(self, elements):
        text = ""
        for value in elements:
            if self._GDOCS_PARAGRAPH in value:
                elements = value.get(self._GDOCS_PARAGRAPH).get(self._GDOCS_ELEMENTS)
                for elem in elements:
                    text += self.read_paragraph_element(element=elem)
            elif self._GDOCS_TABLE in value:
                table = value.get(self._GDOCS_TABLE)
                for row in table.get(self._GDOCS_TABLE_ROWS):
                    cells = row.get(self._GDOCS_TABLE_CELLS)
                    for cell in cells:
                        text += self.read_paragraph_element(element=cell)
            elif self._GDOCS_TABLE_OF_CONTENTS in value:
                table_of_contents = value.get(self._GDOCS_TABLE_OF_CONTENTS)
                text += self.read_paragraph_element(element=table_of_contents)

        return text
