import argparse
from pathlib import Path

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
    default=Path.home(),
)

if __name__ == "__main__":
    args = parser.parse_args()

    document_id = args.document_id

    print(f"[+] Extracting Google Docs Document ID: {document_id}")
    output_folder_gdocs = args.output_folder if args.output_folder else file_paths.GOOGLE_DOC_FOLDER

    google_docs = GoogleDocsDocumentReader(output_folder=output_folder_gdocs)
    filepath = google_docs.extract_document_to_file(document_id=document_id)

    ChineseCSVGenerator(file_to_convert=filepath).generate_csv()
