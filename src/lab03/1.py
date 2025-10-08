def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    if casefold == True: text = text.casefold()
    if yo2e == True: text = text.replace('Ё', 'Е').replace('ё', 'е')
    
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text.replace('\n', ' ').replace('\r', ' ').strip()

casedata = ["ПрИвЕт\nМИр\t", "ёжик, Ёлка", "Hello\r\nWorld", "  двойные   пробелы  "]
for i in casedata: print(normalize(i))

import re

s = "Привет\u200b мир!\n"
clean = re.sub(r'[\x00-\x1F\x7F\u200B\uFEFF]', '', s)
print(repr(clean))