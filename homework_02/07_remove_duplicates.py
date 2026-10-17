# Удаление дубликатов из отсортированного массива на месте.
# slow — позиция для записи следующего уникального элемента.
# fast перебирает массив. Новое значение записываем в nums[slow].
# После прохода убираем оставшийся хвост, удаляя элементы с конца.
# Оба прохода линейные: время O(n), дополнительная память O(1).


def remove_duplicates(nums):
    if len(nums) == 0:
        return nums

    slow = 1

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1

    while len(nums) > slow:
        nums.pop()

    return nums


if __name__ == "__main__":
    numbers = [1, 1, 2, 2, 2, 3, 5, 5]
    print(remove_duplicates(numbers))  # [1, 2, 3, 5]
