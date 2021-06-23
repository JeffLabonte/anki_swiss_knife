import re
import os
from pathlib import Path
from typing import List

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


DATE_REGEX = re.compile(r"[0-9]{3}")


class GoogleDocs:
    """
    Extracts a Google Doc document into a .txt file. That .txt file can
    be parsed into a CSV file. The CSV file is to be imported by Anki afterwards
    """
    SCOPES = [
        "https://www.googleapis.com/auth/documents",
    ]

    VOCAB_START_FLAG = "END FIRST PAGE"

    _FOLDER = "anki_swiss_knife"

    def __init__(self, output_folder):
        self._credentials = None
        self.service = None
        self.output_folder = Path(Path.joinpath(output_folder, self._FOLDER))
        self.init()

    def init(self):
        self._login()
        self._create_folder()

    def _create_folder(self):
        if not os.path.exists(self.output_folder):
            os.mkdir(path=self.output_folder)

    def _login(self):
        filepath = Path(Path.joinpath(Path.home(), ".config", "anki_swiss_tool", "credentials.json"))
        if filepath.exists():
            self._credentials = Credentials.from_service_account_file(filename=filepath, scopes=self.SCOPES)
            self.service = build("docs", "v1", credentials=self._credentials)
        else:
            raise FileNotFoundError()

    def get_document(self, document_id: str):
        return self.service.documents().get(documentId=document_id)

    def is_valid_text(self, element):
        if element.get("paragraph"):
            if element_content := self.extract_content(element=element):
                return element_content != "\n" and DATE_REGEX.match(element_content) is None
        return False

    @staticmethod
    def extract_content(element):
        paragraph_elements = element["paragraph"]["elements"]
        for e in paragraph_elements:
            if e.get("textRun"):
                return e["textRun"]["content"]

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

        contents = [self.extract_content(e) for e in document_contents if self.is_valid_text(element=e)]
        vocabulary_start_index = self.find_page_flag(contents=contents)
        saved_file_path = os.path.join(self.output_folder, f"{document['title']}.txt")
        with open(saved_file_path, "w+") as f:
            f.writelines(contents[vocabulary_start_index + 1:])
            print(f"[+] File saved: {saved_file_path}")
            return saved_file_path
