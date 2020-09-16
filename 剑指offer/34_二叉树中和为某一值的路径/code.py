from collections import deque
from typing import List


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


class Solution:
    # 根节点到叶节点的路径
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []

        # 数字有可能是负数
        def inner(node, s):
            if node:
                path.append(node.val)
                s -= node.val
                if s == 0 and not node.left and not node.right:
                    res.append(list(path))
                inner(node.left, s)
                inner(node.right, s)
                path.pop()

        inner(root, sum)
        return res
