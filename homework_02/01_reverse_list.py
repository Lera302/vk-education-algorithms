# Разворот односвязного списка на месте.
# Сначала запоминаем следующий узел, затем направляем current.next назад.
# prev становится текущим узлом, а current переходит к сохранённому следующему.
# Каждый узел обрабатывается один раз: время O(n), дополнительная память O(1).


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    head = reverse_list(head)

    current = head
    while current is not None:
        print(current.val, end=" ")
        current = current.next
    print()  # 3 2 1
