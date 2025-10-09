import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    text = re.sub(r'[\x00-\x1F\x7F\u200B\uFEFF]', ' ', text).casefold()
    while '  ' in text: text = text.replace('  ', ' ')
    if casefold == True: text = text.casefold()
    if yo2e == True: text = text.replace('Ё', 'Е').replace('ё', 'е')
    return text.strip()
 
def tokenize(text: str): return re.findall( r'\w+(?:-\w+)*', text)

def count_freq(tokens: list[str]):
    token_keys_all = sorted(set(tokens))
    return sorted({token_key: tokens.count(token_key) for token_key in token_keys_all}.items(), key = lambda item: (-item[1], item[0]))

def top_n(freq: dict[str, int], n: int = 5): return sorted(freq.items(), key = lambda item: (-item[1], item[0]))[:n]