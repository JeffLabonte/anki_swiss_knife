def get_translate_client():
    import boto3

    return boto3.client("translate")


def translate_text(
    text_to_translate: str,
    source_language_code: str,
    target_language_code: str,
) -> str:
    response = get_translate_client().translate_text(
        Text=text_to_translate,
        SourceLanguageCode=source_language_code,
        TargetLanguageCode=target_language_code,
    )
    return response["TranslatedText"]
