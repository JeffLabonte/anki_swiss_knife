import os
from pathlib import Path

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


class GoogleDocs:
    SCOPES = [
        "https://www.googleapis.com/auth/documents",
    ]

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

    def extract_document_to_file(self, document_id):
        document = self.get_document(document_id=document_id).execute()
        document_content = document["body"]["content"]
        with open("", "w+") as f:
            print("Test")
