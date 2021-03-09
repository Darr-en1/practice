class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def maxDeath(node):
            if not node:
                return 0
            left = maxDeath(node.left)
            right = maxDeath(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return maxDeath(root) != -1

    def isBalanced1(self, root: TreeNode) -> bool:
        def dfs(node, n):
            if node is None:
                return n
            return max(dfs(node.left, n + 1), dfs(node.right, n + 1))

        if not root:
            return True
        return abs(dfs(root.left, 0) - dfs(root.right, 0)) <= 1 and self.isBalanced(root.left) and self.isBalanced(
            root.right)
