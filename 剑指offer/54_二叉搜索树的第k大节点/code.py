from 剑指offer.tools import arr_to_tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:

        def dfs(node):  # 提前返回
            if not node: return
            dfs(node.right)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            dfs(node.left)

        self.k = k
        dfs(root)
        return self.res


print(Solution().kthLargest(arr_to_tree([3, 1, 4, None, 2]), 1))
