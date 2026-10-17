# Слияние двух отсортированных односвязных списков.
# Выбираем меньшую голову, затем присоединяем меньший из оставшихся узлов.
# Когда один список закончился, присоединяем остаток другого.
# Меняем ссылки существующих узлов, новые узлы внутри функции не создаём.
# Входные списки не имеют циклов и общих узлов.
# Время O(n + m), дополнительная память O(1).


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def merge_lists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val <= list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    tail = head

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1 is not None:
        tail.next = list1
    else:
        tail.next = list2

    return head


if __name__ == "__main__":
    first = ListNode(3, ListNode(6, ListNode(8)))
    second = ListNode(4, ListNode(7, ListNode(9, ListNode(11))))
    head = merge_lists(first, second)

    current = head
    while current is not None:
        print(current.val, end=" ")
        current = current.next
    print()  # 3 4 6 7 8 9 11
