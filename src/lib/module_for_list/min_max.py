def min_max(nums: list[float | int]):
    try:  # если существует список -> вывод кортежа вида: (минимальное число списка, максимальное число списка)
        list
        return ((min(nums)), (max(nums)))
    except ValueError:
        return ValueError  # иначе ошибка
