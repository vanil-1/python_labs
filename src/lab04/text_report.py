from pathlib import Path
from typing import Iterable, Sequence
from collections import Counter
import sys, os, csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))) # добавляет путь к репозиторию с модулями
from module_for_text.text_token import tokenize, normalize


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path) # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return p.read_text(encoding=encoding)

def freq_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like

def sorted_word_per_file(freq: dict[str, int], file_name) -> list[tuple[str, int]]: return [(file_name, pos[0], pos[1]) for pos in sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))]
def sorted_word_total(freq: dict[str, int]) -> list[tuple[str, int]]: return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

def analize_txt_per_file(path, txt = []): 
    all_files = sorted(Path(path).glob('*.txt'), reverse = True)
    for file in all_files: txt += sorted_word_per_file(freq_from_text(read_text(file)), file.name)
    return txt
def analize_txt_total(path, txt = ''):
    for file in Path(path).glob('*txt'): txt += read_text(file)
    return sorted_word_total(freq_from_text(txt))


def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p, rows = Path(path), list(rows)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header: w.writerow(header)
        for r in rows: w.writerow(r)


def text_csv_duo(path_repositories, name_of_csv_file, header):
    txt_per_file, txt_total = analize_txt_per_file(path_repositories), analize_txt_total(path_repositories)
    write_csv(txt_per_file, f"data/lab04/{name_of_csv_file}_report_per_file.csv", header)
    if header: write_csv(txt_total, f"data/lab04/{name_of_csv_file}_report_total.csv", (header[1], header[2]))
    else:  write_csv(txt_total, f"data/lab04/{name_of_csv_file}_report_total.csv", None)
    print(f'Всего слов: {len(txt_per_file)}')
    print(f'Уникальных слов: {len(txt_total)}')
    print('Топ-5:')
    for word_top_5 in txt_total[:5]: print(f'{word_top_5[0]}: {word_top_5[1]}')
    return 'Acsess...'


path_repositories = input('Репозиторий со всеми файлами: ')
name_of_csv_file = input('Имя нового(создать) или старого(переписать) файла-csv: ')
header = tuple(input('Имена столбцов: ').replace(',', ' ').split())

text_csv_duo(path_repositories, name_of_csv_file, header)
