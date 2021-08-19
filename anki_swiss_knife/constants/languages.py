CHINESE_LANGUAGE_CODE = "cmn-CN"
CHINESE_VOICE_ID = "Zhiyu"

CHINESE_UNICODES = "[\u4e00-\u9FFF]"
LATIN_UNICODES = "[\u0000-\u007F]"

CHINESE_TEXT_TO_REMOVE = ("(future tense)",)

CHINESE_WORDS_TO_KEEP = {
    " + V.",
    "+V.",
    "V+",
    " + measure word",
    "+measure word",
    "SF",
    "Quebec City",
    " + W",
    "V. + ",
    "(个)",
    "Harry Potter",
    "Star Wars",
    "+someone.+",
    "Ajd. / V.  + ",
    "(是)",
    "(v./n.)",
    "Baie-Comeau",
}

EXTRA_PUNCTUATION_TO_KEEP = {
    ".",
    ",",
    "!",
    "?",
}
