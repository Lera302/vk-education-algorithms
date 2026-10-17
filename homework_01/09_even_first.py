"""Перенести чётные числа в начало массива на месте.

Порядок чётных сохраняется; порядок нечётных может измениться.
even_index — позиция для следующего найденного чётного числа.
Время: O(n). Дополнительная память: O(1).
"""


def even_first(arr):
    even_index = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[even_index] = arr[even_index], arr[i]
            even_index += 1

    return arr


if __name__ == "__main__":
    numbers = [3, 2, 4, 1, 11, 8, 9]
    print(even_first(numbers))  # [2, 4, 8, 1, 11, 3, 9]
