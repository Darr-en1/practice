from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        tree_list = deque()
        tree_list.append(root)
        res = []
        while tree_list:
            node = tree_list.popleft()
            if node:
                res.append(node.val)
                tree_list.append(node.left)
                tree_list.append(node.right)
            else:
                res.append(None)
        while res and res[-1] is None:
            res.pop()
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree_list = deque()
        tree = TreeNode(data[0]) if data else None
        i = 1
        tree_list.append(tree)
        while i < len(data):
            node = tree_list.popleft()
            # 注意：if data[i] 会出错，因为 0 不是没有节点 只是节点val 为 0
            if data[i] is not None:
                node.left = TreeNode(data[i])
                tree_list.append(node.left)

            if i + 1 < len(data) and data[i + 1] is not None:
                node.right = TreeNode(data[i + 1])
                tree_list.append(node.right)
            i += 2
        return tree


a = Codec().deserialize([])
b = Codec().serialize(a)
print(b)
