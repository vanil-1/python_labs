import re


# NORMALIZE
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    text = re.sub(r"[\x00-\x1F\x7F\u200B\uFEFF]", " ", text).casefold()
    while "  " in text:
        text = text.replace("  ", " ")
    if casefold == True:
        text = text.casefold()
    if yo2e == True:
        text = text.replace("Ё", "Е").replace("ё", "е")
    return text.strip()


normalize_case_text = [
    "ПрИвЕт\nМИр\t",
    "ёжик, Ёлка",
    "Hello\r\nWorld",
    "  двойные   пробелы  ",
]
for case_text in normalize_case_text:
    print(normalize(case_text))
print("-" * 20)


# TOKENIZE
def tokenize(text: str):
    return re.findall(r"\w+(?:-\w+)*", text)


tokenize_case_text = [
    "привет мир",
    "hello,      world!!!",
    "по-настоящему круто",
    "2025 год",
    "emoji 😀 не слово",
]
for case_text in tokenize_case_text:
    print(tokenize(case_text))
print("-" * 20)


# COUNT_FREQ
def count_freq(tokens: list[str]):
    token_keys_all = sorted(set(tokens))
    return sorted(
        {token_key: tokens.count(token_key) for token_key in token_keys_all}.items(),
        key=lambda item: (-item[1], item[0]),
    )


count_freq_case_tokens = [
    ["a", "b", "a", "c", "b", "a"],
    ["bb", "aa", "bb", "aa", "cc"],
]
for case_tokens in count_freq_case_tokens:
    print(count_freq(case_tokens))
print("-" * 20)


# TOP_N
def top_n(freq: dict[str, int], n: int = 5):
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]


top_n_case_freq = [{"b": 2, "a": 3, "c": 1}, {"bb": 2, "cc": 1, "aa": 2}]
for case_freq in top_n_case_freq:
    print(top_n(case_freq))
print("-" * 20)
