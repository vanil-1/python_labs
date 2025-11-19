# lab05

## json_csv

### lib

Используемые библиотеки:

![json_csv.py](/images/lab05/json_csv/lib_json_csv.png)

### json_to_csv(), csv_to_json()

json_to_csv() конвертирует файл формата JSON в файл CSV, модуль path_proccesing() проверяет, существует ли файл, в зависимости от значения второй переменной функции (True/False) создаёт файл или поднимает ошибку FileNotFoundError, а path_is_json() и path_is_csv() проверяют тип файла, его соответствие, в случае не совпадения поднимает ошибку ValueError. Аналогично с функцией csv_to_json(), только функция конвертирует файл формата CSV в файл JSON:

![json_csv.py](/images/lab05/json_csv/json_csv.png)

## csv_xlsx

### lib

Используемые библиотеки:

![csv_xlsx.py](/images/lab05/csv_xlsx/lib_csv_xlsx.png)

### csv_to_xlsx

csv_to_xlsx() конвертирует файл формата CSV в файл XLSX, остальные модули такие же, как и модули в прошлом задании, также добавлена регулировка ширины столбца (минимальная ширина столбца составляет 8 символов), max_len_w - хранит значение длины максимально длинного слова, цикл for index in range(...) определяет количество столбцов и их порядковый номер, а get_column_letter(index) переводит число в название столбца excel (число -> буква ):

![csv_xlsx.py](/images/lab05/csv_xlsx/csv_xlsx.png)