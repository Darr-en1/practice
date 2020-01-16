# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if n == m:
            return head
        _head = head
        last = 1 - n + m
        first = 1

        while first < m - 1:
            first += 1
            head = head.next

        node_1 = head.next

        node_bbb = node_1.next
        node_2 = node_1.next

        while first < n - 1:
            node_3 = node_2.next
            first += 1

            head.next = node_2
            node_2.next = node_1

            node_1 = node_2
            node_2 = node_3

        node_bbb.next = node_3
        return _head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(7)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(2)
    Solution().reverseBetween(head, 4)
