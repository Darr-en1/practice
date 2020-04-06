class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def list_gen(data: list) -> ListNode:
    head = temp = ListNode("head")

    for i in data:
        temp.next = ListNode(i)
        temp = temp.next
    return head.next
