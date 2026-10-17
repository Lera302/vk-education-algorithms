"""Задача флага Нидерландов: сортировка массива из 0, 1 и 2 на месте.

До low расположены нули, от low до mid — единицы,
от mid до high включительно — ещё не обработанные элементы,
после high — двойки. Время: O(n). Дополнительная память: O(1).
"""


def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # Пришедший справа элемент ещё не проверен: mid не двигаем.

    return nums


if __name__ == "__main__":
    numbers = [2, 0, 2, 1, 1, 0]
    print(sort_colors(numbers))  # [0, 0, 1, 1, 2, 2]
