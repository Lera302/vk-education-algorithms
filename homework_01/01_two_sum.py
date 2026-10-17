"""Найти индексы двух разных элементов с суммой target.

Входной массив отсортирован по неубыванию. Индексы начинаются с 0.
Если пары нет, возвращается []. При нескольких парах достаточно одной.
Метод двух указателей. Время: O(n). Дополнительная память: O(1).
"""


def two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []


if __name__ == "__main__":
    print(two_sum([1, 4, 7, 10, 15], 19))  # [1, 4]
