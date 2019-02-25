
"""
    给定一个链表，判断链表中是否有环。
"""
class ListNode(object):
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

    def hasCycle(self, head):
        """
        通过设置不同速度的快、慢两个指针遍历链表。

        慢指针每次移动一步，而快指针每次移动两步。

        判断指针指向的链表对象是否一样判定是否有环。

        时间复杂度：O(n)

        空间复杂度：O(1)
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(node1.hasCycle(node1.next))

