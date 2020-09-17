from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def arr_to_tree(li):
    tree_list = deque()
    tree = Node(li[0]) if li else None
    i = 1
    tree_list.append(tree)
    while i < len(li):
        node = tree_list.popleft()
        if li[i]:
            node.left = Node(li[i])
            tree_list.append(node.left)

        if i + 1 < len(li) and li[i + 1]:
            node.right = Node(li[i + 1])
            tree_list.append(node.right)
        i += 2
    return tree


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        pre = curr = Node(0)
        exist = {}
        while head:
            if head not in exist:
                copy = Node(head.val)
                exist[head] = copy
            curr.next = exist[head]
            if head.random is not None:
                if head.random not in exist:
                    copy = Node(head.random.val)
                    exist[head.random] = copy
                curr.next.random = exist[head.random]

            curr = curr.next
            head = head.next
        return pre.next


if __name__ == '__main__':
    a = arr_to_tree([4, 2, 5, 1, 3])
    Solution().treeToDoublyList(a)
