# lab08

## models

### libs

Используемые библиотеки и модули (всё по классике, анологично предыдущим работам, кроме datetime - работа с датами и временем, dataclasses - работа с классами):

![libs](/images/lab08/models/models_lib.png)

### check_date

Модуль проверяющий корректность формата даты, если формат соответствует установленному формату (по умолчанию установленны следующие форматы: yyyy/mm/dd | yyyy.mm.dd | dd/mm/yyyy | dd.mm.yyyy), то возвращает дату, иначе поднимает ошибку ValueError:

![check_date.py](/images/lab08/models/check_date.png)

### class_fields

Объявление полей класса и их типа данных:

![models.py](/images/lab08/models/models_class_fields.png)

### __post_init__()

Сразу запускается проверка корректности формата даты и соответсявия оценки (0 <= gpa <= 5 и gpa: float | int): 

![models.py](/images/lab08/models/models__post_init__.png)

### age()

Метод класса для расёта возраста студента (datetime.today() - всегда актуальная дата, year - позволяет из даты извлечь год):

![models.py](/images/lab08/models/models_age.png)

### to_dict()

Метод класса, который создаёт словарь с ключами (названия полей) и соответсвующими им значениями (значения полей), с их валидацией:

![models.py](/images/lab08/models/models_to_dict.png)

### clasmethod

Методы для работы с целым классом. from_dict() - присваивает значения словаря полям согласно ключам и названиям полей. __str__() - аналогично __post_init__() запускается сразу, выводит значеня полей в "читаемом" виде:

![models.py](/images/lab08/models/models_classmethod.png)

### models_result

Результат работы кода:

![models.py](/images/lab08/models/models_result.png)

## serialize

### libs

Используемые библиотеки и модули (всё по классике, анологично предыдущим работам, кроме model_student - готовая модель класса студента, совершенного аналогично тому, что представлено в models.py, за исключением тестовых данных):

![libs](/images/lab08/serialize/serialize_lib.png)

### students_to_json and students_from_json

Конвертирует список класса Student с разными объектами в список словарей, а затем записывает в файл JSON. Также конвертирует и в обратную сторону:

![serialize.py](/images/lab08/serialize/serialize_json_list.png)

### serialize_result

Результат работы students_from_json ниже, результаты students_to_json расположены data/lab08/out, а также на скриншоте:

![serialize.py](/images/lab08/serialize/serialize_result.png)

![serialize.py](/images/lab08/serialize/serialize_result_to_json.png)