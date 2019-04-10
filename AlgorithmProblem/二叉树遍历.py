__author__ = 'Darr_en1'

"""
前序遍历：根节点 --> 左子树 -->右子树

中序遍历：左子树  -->根节点 -->右子树

后序遍历： 左子树 -->右子树 -->根节点
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    """
    通过递归的方式
    """
    def preorderTraversal(self, root: TreeNode) -> list:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


    def inorderTraversal(self, root: TreeNode) -> list:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


    def postorderTraversal(self, root: TreeNode) -> list:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


class Solution2:
    """
    通过迭代的方式
    """
    def preorderTraversal(self, root: TreeNode) -> list:
        re_list = []
        stack = []  # 先进后出
        while root or stack:
            while root:
                re_list.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return re_list



    def inorderTraversal(self, root: TreeNode) -> list:
        re_list = []
        stack = []  # 先进后出
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            re_list.append(root.val)
            root = root.right
        return re_list



    def postorderTraversal(self, root: TreeNode) -> list:
        re_list = []
        stack = []  # 先进后出
        while root or stack:
            while root:
                stack.append(root)
                #  能左就左，否则就向右走一步
                root = root.left if root.left is not None else root.right
            root = stack.pop()
            re_list.append(root.val)
            # 栈不空且当前节点是栈顶的左子节点，那么应当继续去访问栈顶的右子节点
            if stack and stack[-1].left == root:
                root = stack[-1].right
            else:
                # 没有右子树或右子树遍历完毕，强迫退栈，输出根节点的值
                root = None
        return re_list

if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(4)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    print(Solution1().preorderTraversal(tree),Solution2().preorderTraversal(tree))
    print(Solution1().inorderTraversal(tree),Solution2().inorderTraversal(tree))
    print(Solution1().postorderTraversal(tree),Solution2().postorderTraversal(tree))





