# lab03

## LIB_WAY

Данные строки кода добавляют путь к репозиторию с библиотеками:

![lib_way](/images/lab03/lib_way.png)

## Task A

### NORMALIZE

Программа нормализрует текст, то есть заменяет все 'ё' на 'е', переводит все буквы в строчные, убирает лишние и двойные пробелы, а также убирает невидимые управляемые символы:

![nor_tok_freq_top_n_normalize.py](/images/lab03/nor_tok_freq_top_n/normalize.png)

### TOKENIZE

Программа разбивает строку на «слова» по небуквенно-цифровым разделителям:

![nor_tok_freq_top_n_tokenize.py](/images/lab03/nor_tok_freq_top_n/tokenize.png)

### COUNT_FREQ

Программа считает частоту слов в строке и выводит словарь (слово: число частоты):

![nor_tok_freq_top_n_count_freq.py](/images/lab03/nor_tok_freq_top_n/count_freq.png)

### TOP_5

Программа считает частоту слов в строке и выводит топ 5 слов по их частоте в порядке убывания:

![nor_tok_freq_top_n_top_n.py](/images/lab03/nor_tok_freq_top_n/top_n.png)

## TASK B

### TEXT_ANALIZATOR

Программа анализирует текст, и выводит общее количество слов, количество уникальных слов, а также топ 5 слов по их частоте:

![text_freq.py](/images/lab03/text_freq/text_freq.png)

## SPECIAL_TASK

### MAIN_CODE: EXTRA_TASK

Программа использует модуль "text_analizator", чтобы проанализировать текст, также как и программа text_freq, но в зависимости от выбора пользователя выдаёт данные либо в строчном виде (0):

![extra_task.py](/images/lab03/extra_task/extra_task_tabl_off.png)

либо в табличном виде:

![extra_task.py](/images/lab03/extra_task/extra_task_tabl_on.png)

p.s. текст для тестирования программы расположен [example.txt](/data/lab03/example.txt)

### LIB_CODE: TEXT_ANALIZATOR

Модуль работает также как и программа text_freq:

![extra_task.py](/images/lab03/extra_task/extra_task_text_analizator.png)