# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
时间复杂度O(n)
空间复杂度O(1)
"""


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        max_list, pre = ListNode(0), ListNode(0)
        last_max_list = max_list
        pre.next = head
        temp = pre
        while temp.next:
            if temp.next.val >= x:
                # last_max_list.next = ListNode(temp.next.val)
                last_max_list.next = temp.next
                last_max_list = last_max_list.next
                temp.next = temp.next.next
            else:
                temp = temp.next
        last_max_list.next = None
        temp.next = max_list.next
        return pre.next

    def partitionOfficial(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        # before and after are the two pointers used to create two list
        # before_head and after_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next

        return before_head.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(7)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(2)
    Solution().partition(head, 4)
