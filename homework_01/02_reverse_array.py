"""Развернуть массив на месте и вернуть его.

Меняем местами крайние элементы, затем сдвигаем указатели к центру.
Время: O(n). Дополнительная память: O(1).
"""


def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(reverse_array(numbers))  # [5, 4, 3, 2, 1]
