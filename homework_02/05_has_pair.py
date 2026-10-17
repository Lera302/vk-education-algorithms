# Есть ли два разных элемента отсортированного массива с суммой target?
# Если сумма мала, двигаем левый указатель к большему числу.
# Если велика, двигаем правый к меньшему. При равенстве пара найдена.
# Указатели только сближаются: время O(n), дополнительная память O(1).


def has_pair(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False


if __name__ == "__main__":
    print(has_pair([1, 4, 7, 10, 15], 19))  # True
    print(has_pair([1, 4, 7, 10, 15], 30))  # False
