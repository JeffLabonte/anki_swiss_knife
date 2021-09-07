import argparse
import os

from anki_swiss_knife.anki_chinese_card_builder import AnkiChineseCardBuilder
from anki_swiss_knife.constants import configs, file_paths, languages
from anki_swiss_knife.google_docs_document_reader import GoogleDocsDocumentReader
from anki_swiss_knife.helper import files
from anki_swiss_knife.text_to_speech import TextToSpeech


def initial_startup(force: bool = False):
    files.create_initial_file(
        file_path=configs.CONFIGURATION_FILE_INI,
        content=configs.DEFAULT_CONFIGURATIONS,
        force=force,
    )


def create_cli_parser():
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

    parser.add_argument(
        "--text-to-speech",
        dest="text_to_speech",
        help="Do you want to generate a csv with text-to-speech?",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "--chinese_not_first",
        dest="chinese_not_first",
        help="Set Chinese to back en English to Front",
        action="store_false",
        default=True,
    )
    parser.add_argument(
        "--reset-configs",
        dest="reset_configs",
        help=f"Reset to default configs:\n{configs.DEFAULT_CONFIGURATIONS}",
        action="store_true",
        default=False,
    )

    return parser


if __name__ == "__main__":
    args = create_cli_parser().parse_args()

    document_id = args.document_id

    print(f"[+] Extracting Google Docs Document ID: {document_id}")
    gdocs_folder_path = os.path.join(args.output_folder, file_paths.GOOGLE_DOC_FOLDER_NAME)

    google_docs = GoogleDocsDocumentReader(output_folder=gdocs_folder_path)
    gdoc_filepath = google_docs.extract_document_to_file(document_id=document_id)

    csv_filepath = AnkiChineseCardBuilder(
        file_to_convert=gdoc_filepath,
        is_chinese_first_column=args.chinese_not_first,
    ).generate_csv()

    if args.text_to_speech:
        text_to_speech = TextToSpeech(
            language_code=languages.CHINESE_LANGUAGE_CODE,
            voice_id=languages.CHINESE_VOICE_ID,
            csv_filepath=csv_filepath,
        )
        text_to_speech.generate_csv_with_speech()
