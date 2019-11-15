# 找到两个单链表相交的起始节点。存在返回起始节点不存在返回None


class Solution(object):
    """
        如果两个链表没有交点，返回 null.
        在返回结果后，两个链表仍须保持原有的结构。
        可假定整个链表结构中没有循环。
        程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

        https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/dong-hua-yan-shi-160-xiang-jiao-lian-biao-by-user7/
    """
    @staticmethod
    def get_intersection_node(head_a, head_b):
        a, b = head_a, head_b
        while a != b:
            a = a.next if a else head_b
            b = b.next if b else head_a
        return a
