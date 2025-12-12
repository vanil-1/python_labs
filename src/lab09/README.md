# lab09

## group

### libs

Используемые библиотеки и модули (всё по классике, анологично предыдущим работам, кроме функции inicialPath модуля pathProccecing), также импортирован класс Student:

![libs](/images/lab09/libs/group_lib.png)

### inicialPath

Работает анлогично pathProccesing, но проще, и только создаёт файл, если его нет:

![inicialPath](/images/lab09/libs/inicialPath.png)

### group fields

Объявление полей класса и их типа данных:

![group.py](/images/lab09/group_fields.png)


### __init__()

Сразу запускается проверка корректности расширения файла, а также наличие заголовков: 

![group.py](/images/lab09/group__init__.png)

### _read_all()

Метода, считывающий строки CS файла:

![group.py](/images/lab09/group_read_all.png)

### data

Входные данные для тестирования:

![data](/images/lab09/group_data.png)

### list()

Метод, который конвертирует CSV файлы в список python, элементы которого - класс Student:

![group.py](/images/lab09/group_list/group_list.png)

Результат работы:

![group.py](/images/lab09/group_list/group_list_out.png)

### add()

Метод, который добавляет элемент - класс Student в файл CSV:

![group.py](/images/lab09/group_add/group_add.png)

Результат работы:

![group.py](/images/lab09/group_add/group_add_out.png)

### find()

Метод, который находит студента по подстрокам ФИО:

![group.py](/images/lab09/group_find/group_find.png)

Результат работы:

![group.py](/images/lab09/group_find/group_find_out.png)

### remove()

Метод, который удаляет студента по подстрокам поля fio класс Student:

![group.py](/images/lab09/group_remove/group_remove.png)

Результат работы:

![group.py](/images/lab09/group_remove/group_remove_out.png)

### update()

Метод, который обновляет поля студента, в зависимости от значений полей Student, если они иные, то меняет:

![group.py](/images/lab09/group_update/group_update.png)

Результат работы:

![group.py](/images/lab09/group_update/group_update_out.png)

### stats()

Метод, который собирает ститистику по файлу:

![group.py](/images/lab09/group_stats/group_stats.png)

Результат работы:

![group.py](/images/lab09/group_stats/group_stats_out.png)