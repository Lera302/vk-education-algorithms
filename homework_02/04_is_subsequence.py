# Проверяем, можно ли получить b, добавив символы в a без перестановки.
# i указывает на следующий искомый символ a, j перебирает символы b.
# При совпадении сдвигаем i, а j сдвигаем всегда. В конце должны найти всю a.
# Время O(len(b)), дополнительная память O(1).


def is_subsequence(a, b):
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
        j += 1

    return i == len(a)


if __name__ == "__main__":
    print(is_subsequence("кот", "крот"))  # True
    print(is_subsequence("кот", "ток"))   # False
