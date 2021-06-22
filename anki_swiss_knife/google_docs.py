import os
from pathlib import Path

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


class GoogleDocs:
    SCOPES = [
        "https://www.googleapis.com/auth/documents",
    ]

    def __init__(self):
        self.creds = None
        self.service = None

        self._login()

    def _login(self):
        filepath = Path(Path.joinpath(Path.home(), ".config", "anki_swiss_tool", "credentials.json"))
        if filepath.exists():
            self.creds = Credentials.from_service_account_file(filename=filepath, scopes=self.SCOPES)
            self.service = build("docs", "v1", credentials=self.creds)
        else:
            raise FileNotFoundError()

    def get_document(self, document_id: str):
        return self.service.documents().get(documentId=document_id)