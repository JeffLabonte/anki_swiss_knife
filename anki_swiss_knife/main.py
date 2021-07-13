import argparse
import os

from anki_swiss_knife.chinese_csv_generator import ChineseCSVGenerator
from anki_swiss_knife.constants import file_paths
from anki_swiss_knife.google_docs_document_reader import GoogleDocsDocumentReader


parser = argparse.ArgumentParser(description="What document do you want to parse")

parser.add_argument(
    "--gdocs-document-id",
    dest="document_id",
    help="Google Docs Document ID you whish to extract",
    type=str,
    required=True,
)
parser.add_argument(
    "--output-folder",
    dest="output_folder",
    help="Where to create output folder",
    type=str,
    default=file_paths.DEFAULT_BASE_FOLDER,
)

if __name__ == "__main__":
    args = parser.parse_args()

    document_id = args.document_id

    print(f"[+] Extracting Google Docs Document ID: {document_id}")
    gdocs_folder_path = os.path.join(args.output_folder, file_paths.GOOGLE_DOC_FOLDER_NAME)

    google_docs = GoogleDocsDocumentReader(output_folder=gdocs_folder_path)
    filepath = google_docs.extract_document_to_file(document_id=document_id)

    ChineseCSVGenerator(file_to_convert=filepath).generate_csv()
