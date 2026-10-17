"""Сумма целых чисел от 1 до n включительно.

Вводная задача семинара: n = 1 000 000.
Предполагается, что n — целое неотрицательное число.
Время: O(n). Дополнительная память: O(1).
"""


def sum_numbers(n):
    total = 0
    for number in range(1, n + 1):
        total += number
    return total


if __name__ == "__main__":
    print(sum_numbers(1_000_000))  # 500000500000
