"""Найти минимальную длину непрерывного подмассива с суммой >= target.

nums содержит положительные целые числа; target > 0.
Если подходящего подмассива нет, вернуть 0.
Скользящее окно. Время: O(n). Дополнительная память: O(1).
"""


def min_subarray_length(nums, target):
    left = 0
    current_sum = 0
    min_length = len(nums) + 1

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            window_length = right - left + 1
            if window_length < min_length:
                min_length = window_length
            current_sum -= nums[left]
            left += 1

    if min_length == len(nums) + 1:
        return 0
    return min_length


if __name__ == "__main__":
    print(min_subarray_length([2, 3, 1, 2, 4, 3], 7))  # 2
