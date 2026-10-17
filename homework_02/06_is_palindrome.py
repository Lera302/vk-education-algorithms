# Проверка палиндрома двумя указателями.
# Сравниваем крайние символы, затем переходим к следующей паре ближе к центру.
# Одного несовпадения достаточно, чтобы вернуть False.
# Сравниваем символы как есть: регистр, пробелы и знаки учитываются.
# Время O(n), дополнительная память O(1).


def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    print(is_palindrome("топот"))  # True
    print(is_palindrome("слово"))  # False
