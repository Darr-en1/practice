__author__ = 'Darr_en1'

""" 

链表反转

"""
class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next


class RecursionSolution:
    """
    复杂性分析

    时间复杂度： O（n）

    空间复杂度： O（n）

    """
    def reverse_list(self, head: ListNode, tail=None) -> ListNode:
        """

        :param head: 被反转链表
        :param tail: 反转后链表对象
        :return: 反转后链表
        """
        head.next, tail, head = tail, head, head.next
        return self.reverse_list(head, tail) if head else tail

class NonRecursionSolution:
    """
    复杂性分析

    时间复杂度： O（n）

    空间复杂度： O（1）

    """
    def reverse_list(self, head: ListNode) -> ListNode:
        p = None
        while head: head.next, p, head = p, head, head.next
        return p


if __name__ == '__main__':
    listNode = ListNode(4,ListNode(3,ListNode(5,ListNode(1,ListNode(2)))))
    re_reverse_list = NonRecursionSolution().reverse_list(listNode)
    re_list = []
    while re_reverse_list:
        re_list.append(re_reverse_list.val)
        re_reverse_list=re_reverse_list.next

    print(re_list)
