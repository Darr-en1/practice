class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def inner(a, b):
            if b is None:
                return True
            if a is None or a.val != b.val:
                return False
            return inner(a.left, b.left) and inner(a.right, b.right)

        return bool(A and B) and (inner(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))


if __name__ == '__main__':
    tree_a = TreeNode(3)
    tree_a.left = TreeNode(4)
    tree_a.right = TreeNode(5)
    tree_a.left.left = TreeNode(1)
    tree_a.left.right = TreeNode(2)
    tree_a.left.left.left = TreeNode(7)

    tree_b = TreeNode(1)
    tree_b.left = TreeNode(7)

    print(Solution().isSubStructure(tree_a, tree_b))
