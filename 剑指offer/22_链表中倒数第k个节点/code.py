class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        a, b = 0, k
        pre = head
        while a < k and head:
            head = head.next
            a += 1
        while head:
            pre = pre.next
            head = head.next
        return pre
