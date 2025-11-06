from pathlib import Path
from typing import Iterable, Sequence
from collections import Counter
import sys, os, csv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))) # добавляет путь к репозиторию с модулями
from module_for_text.text_token import tokenize, normalize

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path) # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return p.read_text(encoding=encoding)

def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like

def sorted_word_counts(freq: dict[str, int], file_name) -> list[tuple[str, int]]: return [(file_name, pos[0], pos[1]) for pos in sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))]

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p, rows = Path(path), list(rows)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None: w.writerow(header)
        for r in rows: w.writerow(r)

def analize_txt(path): 
    files_sort, all_files = [], sorted(Path(path).glob('*.txt'), reverse = True)
    for file in all_files: files_sort = files_sort + sorted_word_counts(frequencies_from_text(read_text(file)), file.name)
    return files_sort


path_to_repositories = input('Репозиторий со всеми файлами: ')
name_of_csv_file = input('Имя нового(создать) или старого(переписать) файла-csv: ')
header = tuple(input('Имена столбцов: ').replace(',', ' ').split())
txt = analize_txt(path_to_repositories)
write_csv(txt, f"data/lab04/{name_of_csv_file}.csv", header)  # создаст CSV
print('Acsess...')