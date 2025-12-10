import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    text = re.sub(r"[\x00-\x1F\x7F\u200B\uFEFF]", " ", text).casefold()
    while "  " in text:
        text = text.replace("  ", " ")
    if casefold == True:
        text = text.casefold()
    if yo2e == True:
        text = text.replace("Ё", "Е").replace("ё", "е")
    return text.strip()
