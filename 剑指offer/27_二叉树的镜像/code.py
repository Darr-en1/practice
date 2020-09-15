class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root


if __name__ == '__main__':
    tree_a = TreeNode(3)
    tree_a.left = TreeNode(4)
    tree_a.right = TreeNode(5)
    tree_a.left.left = TreeNode(1)
    tree_a.left.right = TreeNode(2)
    tree_a.left.left.left = TreeNode(7)

    trre_b = Solution().mirrorTree(tree_a)
