"""Слить два отсортированных массива в новый отсортированный массив.

Исходные массивы отсортированы по неубыванию и не изменяются.
Время: O(n + m). Память под результат: O(n + m).
Помимо результата используется O(1) дополнительной памяти.
"""


def merge_arrays(arr1, arr2):
    merged = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Добавляем оставшиеся элементы по одному, без создания срезов.
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged


if __name__ == "__main__":
    print(merge_arrays([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
