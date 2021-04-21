from 剑指offer.tools import arr_to_tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth1(self, root: TreeNode) -> int:
        def inner(node, deep):
            if node is None:
                return deep

            deep += 1
            return max(inner(node.left, deep), inner(node.right, deep))

        return inner(root, 0)

    def maxDepth(self, root: TreeNode) -> int:  # 更加优美
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


print(Solution().maxDepth1(arr_to_tree([3, 9, 20, None, None, 15, 7])))
