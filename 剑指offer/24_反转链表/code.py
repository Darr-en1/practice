class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def reverseList1(self, head: ListNode) -> ListNode:
        new_head = None

        while head:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
        return new_head
