from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        ino_dict = {val: idx for idx, val in enumerate(inorder)}

        def inner(root_idx, left, right):
            if left > right:
                return
            root_idx_in_inorder = ino_dict[preorder[root_idx]]
            root = TreeNode(preorder[root_idx])
            # 中序遍历中，根节点前都是左子树，计算根节点前左子树个数 i - in_left ，
            # 先序遍历中，pre_root 位置加上左子树个数可得最后一个左子树位置，下一个为右子树头节点
            root.left = inner(root_idx + 1, left, root_idx_in_inorder - 1)
            root.right = inner(root_idx_in_inorder - left + root_idx + 1, root_idx_in_inorder + 1, right)
            return root

        return inner(0, 0, len(inorder) - 1)


if __name__ == '__main__':
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7, 2, 1, 5, 3, 8, 6]

    r = Solution().buildTree(preorder, inorder)
    pass
