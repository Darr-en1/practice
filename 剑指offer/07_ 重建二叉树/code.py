from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.po = preorder
        self.dic = {val: idx for idx, val in enumerate(inorder)}
        return self.recur(0, 0, len(inorder) - 1)

    def recur(self, pre_root, in_left, in_right):
        if in_left > in_right: return
        root = TreeNode(self.po[pre_root])
        i = self.dic[self.po[pre_root]]
        root.left = self.recur(pre_root + 1, in_left, i - 1)
        # 中序遍历中，根节点前都是左子树，计算根节点前左子树个数 i - in_left ，
        # 先序遍历中，pre_root 位置加上左子树个数可得最后一个左子树位置，下一个为右子树头节点
        root.right = self.recur(i - in_left + pre_root + 1, i + 1, in_right)
        return root


if __name__ == '__main__':
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7, 2, 1, 5, 3, 8, 6]

    r = Solution().buildTree(preorder, inorder)
    pass
