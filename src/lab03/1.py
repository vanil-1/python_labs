def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    if casefold == True: text = text.casefold()
    while '  ' in text:
        text=text.replace('  ', ' ')
    if yo2e == True: text = text.replace('Ё', 'Е').replace('ё', 'е')
    return text.replace('\n', ' ').replace('\r', ' ').strip()



casedata = ["ПрИвЕт\nМИр\t", "ёжик, Ёлка", "Hello\r\nWorld", "  двойные   пробелы  "]
for i in casedata: print(normalize(i))