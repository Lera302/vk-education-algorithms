"""Отсортировать на месте массив, содержащий только 0 и 1.

Используем два указателя: нули оставляем слева, единицы справа.
Время: O(n). Дополнительная память: O(1).
"""


def sort_binary_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr


if __name__ == "__main__":
    numbers = [1, 0, 1, 0, 0, 1]
    print(sort_binary_array(numbers))  # [0, 0, 0, 1, 1, 1]
