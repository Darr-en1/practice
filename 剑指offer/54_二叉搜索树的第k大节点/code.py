from 剑指offer.tools import arr_to_tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        a = []

        def aa(node):
            if node:
                aa(node.right)
                a.append(node.val)
                aa(node.lefat)

        aa(root)
        return a[k - 1]

        # def dfs(root):  提前返回
        #     if not root: return
        #     dfs(root.right)
        #     if self.k == 0: return
        #     self.k -= 1
        #     if self.k == 0: self.res = root.val
        #     dfs(root.left)
        #
        # self.k = k
        # dfs(root)
        # return self.res


print(Solution().kthLargest(arr_to_tree([3, 1, 4, None, 2]), 1))
