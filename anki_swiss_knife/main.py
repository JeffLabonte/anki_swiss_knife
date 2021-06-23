import argparse
from pathlib import Path

from anki_swiss_knife.csv_generator import CSVGenerator
from anki_swiss_knife.google_docs import GoogleDocs

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
    google_docs = GoogleDocs(output_folder=args.output_folder)
    filepath = google_docs.extract_document_to_file(document_id=document_id)
    CSVGenerator(file_to_convert=filepath).generate_csv()
