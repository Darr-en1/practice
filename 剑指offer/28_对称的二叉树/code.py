class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def compare(left, right):
            if left is None and right is None:
                return True

            if left is None or right is None or left.val != right.val:
                return False
            else:
                return compare(left.left, right.right) and compare(left.right, right.left)

        return compare(root.left, root.right) if root else True


if __name__ == '__main__':
    tree_a = TreeNode(1)
    tree_a.left = TreeNode(2)
    tree_a.right = TreeNode(2)
    tree_a.left.left = TreeNode(3)
    tree_a.left.right = TreeNode(4)
    tree_a.right.left = TreeNode(4)
    tree_a.right.right = TreeNode(3)

    trre_b = Solution().isSymmetric(tree_a)
    print(trre_b)
