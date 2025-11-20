import sys, os, argparse
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib')))
from pathProccesing import pathProccesing
from module_for_text.text_analizator import text_analizator

def main():
    parser = argparse.ArgumentParser(description = "CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest = "command")

    cat_parser = subparsers.add_parser("cat", help = "Вывести содержимое файла")
    cat_parser.add_argument("--input", required = True)
    cat_parser.add_argument("-n", action="store_true", help = "Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help = "Частоты слов")
    stats_parser.add_argument("--input", required = True)
    stats_parser.add_argument("--top", type = int, default = 5)

    args = parser.parse_args()

    path_in = pathProccesing(f'C:/Users/devAll/Desktop/python_labs/data/lab06/samples/{args.input}', False, ('.txt'))
    try:
        with path_in.open(encoding = "utf-8") as f:
            if args.command == "cat":
                if args.n == True: 
                    for i, row in enumerate(f, start = 0): print(f"{i}. {row}", end="")
                else: 
                    for row in f: print(row)
            elif args.command == "stats":
                text = "".join(f.readlines()) 
                text_analizator(text, args.top)
    except: print(path_in)

main()