# lab034

## io_txt_csv

### lib

Используемые библиотеки:

![io_txt_csv.py](/images/lab04/io_txt_csv/lib_io_txt_csv.png)

### read_text(), frequencies_from_text(), sort_word_counts_per_file()

read_text() считывает текст из файла, переводя его в тип str. frequencies_from_text() анализирует текст при помощи модуля tokenize() и normalize() и создаёт словарь с соответствующими значениями. sort_word_counts_per_file() сортирует словарь (по ключам в алфавитном порядке, по значениям в убывающем порядке):

![io_txt_csv.py](/images/lab04/io_txt_csv/text_proccesing.png)

### write_csv(), analize_txt_per_file(), text_csv_base()

write_csv() записываетв все данные в формате CSV, с учётом заголовка, в случае, если указанного файла не существует, то создаёт новый файл. analize_txt_per_file() дополнительная сортировка с учётом имени считываемого файла. text_csv_base() использует write_csv() и записывает отсортированный файл CSV с учётом имени файла: 

![io_txt_csv.py](/images/lab04/io_txt_csv/write_csv.png)

### 'input'

Ввод репозитория с обрабатываемыми файлами, имени новго или существующего файла, а также название заголовка:

![io_txt_csv.py](/images/lab04/io_txt_csv/input.png)

## text_report

### lib

Используемые библиотеки:

![text_report.py](/images/lab04/text_report/lib_text_report.png)

### read_text(), freq_from_text(), sorted_word_per_file(), sorted_word_total(), analize_txt_per_file(), analize_txt_total()

Всё аналогично функциям из прошлого задания кроме 2-х функций: sorted_word_total() и analize_txt_total(). Они не учитывают название файлов, сортируя все значения из всех файлов.

![text_report.py](/images/lab04/text_report/text_proccesing_total.png)

### write_csv(), text_csv_duo()

Аналогично функциям из прошлого задания, но text_csv_duo() выдаёт дополнительный отчёт, сводку данных об анализе текстового файла.

![text_report.py](/images/lab04/text_report/write_csv_total.png)

### 'input'

Ввод репозитория с обрабатываемыми файлами, имени новго или существующего файла, а также название заголовка:

![text_report.py](/images/lab04/text_report/input_total.png)