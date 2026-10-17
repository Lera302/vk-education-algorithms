# Удаляем все узлы со значением val, как в решении семинара.
# Если val находится в голове, передвигаем голову до первого другого значения.
# Внутри списка пропускаем удаляемый узел: current.next = current.next.next.
# После удаления current не двигаем: следующий узел тоже может содержать val.
# Время O(n), дополнительная память O(1), новый список не создаётся.


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def remove_elements(head, val):
    while head is not None and head.val == val:
        head = head.next

    current = head
    while current is not None and current.next is not None:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next

    return head


if __name__ == "__main__":
    head = ListNode(2, ListNode(1, ListNode(2, ListNode(3))))
    head = remove_elements(head, 2)

    current = head
    while current is not None:
        print(current.val, end=" ")
        current = current.next
    print()  # 1 3
