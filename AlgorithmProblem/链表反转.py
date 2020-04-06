from util.list import ListNode, list_gen


def reversal(head: ListNode):
    if head is None or head.next is None:
        return head

    cur = reversal(head.next)

    head.next.next = head
    head.next = None # 防止循环
    return cur


def reversal1(head: ListNode):
    pre = None
    cur = head
    # 遍历链表，while循环里面的内容其实可以写成一行
    # 这里只做演示，就不搞那么骚气的写法了
    while cur:
        # 记录当前节点的下一个节点ccccccccccccccccccccc   zzzz
        tmp = cur.next
        # 然后将当前节点指向pre
        cur.next = pre
        # pre和cur节点都前进一位
        pre = cur
        cur = tmp
    return pre


a = list_gen([1, 2, 3, 4, 5, 6, 7])

b = reversal(a)
while b:
    print(b.val)
    b = b.next
