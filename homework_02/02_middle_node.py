# Поиск середины односвязного списка.
# slow делает один шаг, fast — два. Когда fast дошёл до конца,
# slow прошёл примерно половину списка и находится в середине.
# При чётной длине возвращаем второй из двух центральных узлов.
# Время O(n), дополнительная память O(1), новые узлы не создаются.


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def middle_node(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    middle = middle_node(head)
    if middle is not None:
        print(middle.val)  # 3
