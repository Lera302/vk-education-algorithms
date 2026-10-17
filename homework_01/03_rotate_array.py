"""Циклически сдвинуть массив вправо на k позиций на месте.

Направление соответствует примеру семинара: при k = 3 последние
три элемента переходят в начало. k — целое неотрицательное число.
Три разворота. Время: O(n). Дополнительная память: O(1).
"""


def reverse_part(arr, left, right):
    # Разворачиваем участок от left до right включительно.
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def rotate_array(arr, k):
    n = len(arr)
    if n == 0:
        return arr

    k %= n
    if k == 0:
        return arr

    reverse_part(arr, 0, n - 1)
    reverse_part(arr, 0, k - 1)
    reverse_part(arr, k, n - 1)
    return arr


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print(rotate_array(numbers, 3))  # [5, 6, 7, 1, 2, 3, 4]
