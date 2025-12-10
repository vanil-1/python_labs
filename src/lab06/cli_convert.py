import sys, os, argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lib")))
from json_csv_xlsx.json_csv_xlsx import csv_to_json, json_to_csv, csv_to_xlsx


def main():
    main_path = "C:/Users/devAll/Desktop/python_labs/data/lab06/"

    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help="Конвертировать JSON в CSV")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json", help="Конвертировать CSV в JSON")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx", help="Конвертировать CSV в XLSX")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()
    path_in, path_out = (
        f"{main_path}samples/{args.input}",
        f"{main_path}out/{args.output}",
    )

    if args.cmd == "json2csv":
        json_to_csv(path_in, path_out)
    elif args.cmd == "csv2json":
        csv_to_json(path_in, path_out)
    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(path_in, path_out)


main()
