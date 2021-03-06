[![CI](https://github.com/JeffLabonte/anki_swiss_knife/actions/workflows/ci.yml/badge.svg)](https://github.com/JeffLabonte/anki_swiss_knife/actions/workflows/ci.yml) [![Lint](https://github.com/JeffLabonte/anki_swiss_knife/actions/workflows/black.yml/badge.svg)](https://github.com/JeffLabonte/anki_swiss_knife/actions/workflows/black.yml) [![codecov](https://codecov.io/gh/JeffLabonte/anki_swiss_knife/branch/main/graph/badge.svg?token=976XZBSN8I)](https://codecov.io/gh/JeffLabonte/anki_swiss_knife) [![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/JeffLabonte/anki_swiss_knife.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/JeffLabonte/anki_swiss_knife/context:python)
 [![Total alerts](https://img.shields.io/lgtm/alerts/g/JeffLabonte/anki_swiss_knife.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/JeffLabonte/anki_swiss_knife/alerts/) [![CodeQL](https://github.com/JeffLabonte/anki_swiss_knife/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/JeffLabonte/anki_swiss_knife/actions/workflows/codeql-analysis.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/251722c1151d96623c92/maintainability)](https://codeclimate.com/github/JeffLabonte/anki_swiss_knife/maintainability)

**STILL A WORK IN PROGRESS**

## Anki Swiss Knife

笔记 : 我在学中文，也这个文件我要尝试翻译

NOTE : I am learning Chinese. I will (want) try to translate this document.

### Description/描写

This project is currently only grabbing a document that has Chinese characters plus translations that I share with my teacher.

The structure of the document is the following:

你好 Nǐ hǎo Hi
...

I take those translations and make it into a CSV file. I added the option to add text-to-speech to help me remember the words and memorise the pronounciation. It was based on some code created by @marcaube.

### Setup

You need to have access to Google Cloud. You must create a service account and give access to your document using the service account email

### Configurations

* General:
  * text-with-speech
    * Default: True
    * Description: Create extra CSV file with text-to-speech.
  * swap-source-destination-language
    * Default: True
    * Description: Create extra CSV filew where Language source is swapped with destination. i.e: ZH -> EN will be EN -> ZH
  * enable-google-docs
    * Default: True
    * Description: Enable google docs to retrieve phrases. You need to specify your `credential_file` from Google and the `document-id`.
  * enable-fluentu
    * Default: False
    * Description: Enable fluentu to retrieve saved words from. You need specify the `username` and the `password` within the `FluentU` section.
  