from anki_swiss_knife.google_docs import GoogleDocs


def test__google_docs__login__should_be_sucessful():
    google_docs_api = GoogleDocs()

    assert google_docs_api._credentials.expired is False