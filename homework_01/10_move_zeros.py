"""Перенести все нули в конец массива на месте.

Относительный порядок ненулевых элементов сохраняется.
write — позиция для следующего ненулевого элемента.
Время: O(n). Дополнительная память: O(1).
"""


def move_zeros(arr):
    write = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[write], arr[i] = arr[i], arr[write]
            write += 1

    return arr


if __name__ == "__main__":
    numbers = [0, 0, 1, 0, 3, 12]
    print(move_zeros(numbers))  # [1, 3, 12, 0, 0, 0]
