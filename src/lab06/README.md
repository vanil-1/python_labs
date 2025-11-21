# lab06

## cli_text

### pathProccesing

Проверяет расширение файла, несоответствие = ValuError. В случае соответствия, проверяет существует ли файл, если нет, то в зависимости от значения path_out создаёт новый файл(path_out = True), или поднимает ошибку FileNotFoundError. Если файл существует или создан, то возвращает путь к до файла:

![pathProccesing.py](/images/lab06/cli_text/cli_text_path.png)

### code cli_text

В зависимости от вводимой команды в консоли выполняет одну из 2-х команд:

![cli_text.py](/images/lab06/cli_text/cli_text_code.png)

#### cat

Выводит содержимое файла:

![cli_text.py](/images/lab06/cli_text/cat.png)

Если указан флаг -n, то нумерует строки:

![cli_text.py](/images/lab06/cli_text/cat_n.png)

#### stats

Выводит статистику текста, т.е. общее количество слов, количество уникальных слов, а также топ повторяющихся слов(количество выводимых слов из топа также задаётся, при помощи --top):

![cli_text.py](/images/lab06/cli_text/stats_tabl_off.png)

Если ввести после запуска кода 0 - статистика в виде текста (как представлено выше), если 1 - статистика в виде таблицы (как представлено ниже):

![cli_text.py](/images/lab06/cli_text/stats_tabl_on.png)

#### help

Вывод команд и их функций:

![cli_text.py](/images/lab06/cli_text/text_help.png)

#### Errors

Неправильное расширение файла:

![cli_text.py](/images/lab06/cli_text/text_ValueError.png)

Неправильный путь к файлу или файл не существует:

![cli_text.py](/images/lab06/cli_text/text_FileNotFoundError.png)

## cli_convert

### pathProccesing

Тот же самый модуль, что описан ранее:

![pathProccesing.py](/images/lab06/cli_convert/cli_convert_path.png)

### code cli_convert

Использован модуль json_csv_xlsx.py, с функциями конвертации JSON <-> CSV и CSV -> XLSX (из ЛР5). В зависимости от вводимой команды в консоли выполняет одну из 3-х команд:

![cli_convert.py](/images/lab06/cli_convert/cli_convert_code.png)

#### json_csv_xlsx.py

Ниже представлен модуль, объединяющий все функции конверции из ЛР5 (также в коде используется функция pathProccesing из одноимённого модуля, который был описан ранее):

![json_csv_xlsx.py](/images/lab06/cli_convert/cli_lib_convert.png)

#### json2csv

Конвертирует файл JSON в файл CSV:

![cli_convert.py](/images/lab06/cli_convert/cli_json2csv.png)

#### csv2json

Конвертирует файл CSV в файл JSON:

![cli_convert.py](/images/lab06/cli_convert/cli_csv2json.png)

#### csv2xlsx

Конвертирует файл CSV в файл XLSX:

![cli_convert.py](/images/lab06/cli_convert/cli_csv2xlsx.png)

#### help

Вывод команд и их функций:

![cli_convert.py](/images/lab06/cli_convert/convert_help.png)

#### Errors

Неправильное расширение файла:

![cli_convert.py](/images/lab06/cli_convert/convert_ValueError.png)

Неправильный путь к файлу или файл не существует:

![cli_convert.py](/images/lab06/cli_convert/convert_FileNotFoundError.png)