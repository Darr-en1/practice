from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        return self.reversePrint(head.next) + [head.val] if head else []

    def reversePrint1(self, head: ListNode) -> List[int]:

        def recur(node):
            if not node:
                return
            recur(node.next)
            res.append(node.val)

        res = []
        recur(head)
        return res
