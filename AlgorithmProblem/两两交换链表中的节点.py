# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head_list = ListNode(0)
        head_list.next = head

        temp = head_list

        while temp.next and temp.next.next:
            node_1 = temp.next
            node_2 = temp.next.next
            temp.next = node_2
            node_1.next = node_2.next
            node_2.next = node_1
            temp = node_1
        return head_list.next

    def swapPairsRecursion(self, head):
        """
        :type head: ListNode
        :rtype: Lis tNode
        """
        if head and head.next:
            node_2 = head.next
            head.next = self.swapPairsRecursion(node_2.next)
            node_2.next = head
            return node_2
        return head
