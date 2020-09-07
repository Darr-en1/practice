class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre = curr = ListNode(0)
        more = 0
        while l1 or l2 or more:
            num = (l1.val if l1 else 0) + (l2.val if l2 else 0) + more
            curr.next = ListNode(num % 10)
            curr = curr.next
            more = num // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return pre.next


def arrToList(arr):
    pre = curr = ListNode(0)
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return pre.next


arr1 = [2, 4, 3]
arr2 = [5, 6, 4]

l1 = arrToList(arr1)
l2 = arrToList(arr2)
print(Solution().addTwoNumbers(l1, l2))
pass
