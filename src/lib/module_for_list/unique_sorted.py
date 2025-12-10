def unique_sorted(nums: list[float | int]):
    try:  # если существует список -> вывод отсортированного списка с уникальными значениями
        list
        return [number for number in sorted(set(nums))]
    except ValueError:
        return []
