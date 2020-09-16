from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def arr_to_tree(li):
    tree_list = deque()
    tree = TreeNode(li[0]) if li else None
    i = 1
    tree_list.append(tree)
    while i < len(li):
        node = tree_list.popleft()
        if li[i]:
            node.left = TreeNode(li[i])
            tree_list.append(node.left)

        if i + 1 < len(li) and li[i + 1]:
            node.right = TreeNode(li[i + 1])
            tree_list.append(node.right)
        i += 2
    return tree
