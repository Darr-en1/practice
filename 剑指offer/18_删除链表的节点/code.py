class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:

        if head.val == val:
            return head.next
        pre, curr = head, head.next
        while curr:
            if curr.val == val:
                pre.next = curr.next
                return head
            pre, curr = curr, curr.next
