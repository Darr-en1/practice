from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def arr_to_tree(li):
    tree_list = deque()
    tree = Node(li[0]) if li else None
    i = 1
    tree_list.append(tree)
    while i < len(li):
        node = tree_list.popleft()
        if li[i]:
            node.left = Node(li[i])
            tree_list.append(node.left)

        if i + 1 < len(li) and li[i + 1]:
            node.right = Node(li[i + 1])
            tree_list.append(node.right)
        i += 2
    return tree


class Solution:
    # 二叉搜索树中序遍历是顺序数组
    # 节点的right 等同于 next
    # 节点的left 等同于 pre
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)  # 递归左子树
            if hasattr(self, "pre"):  # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else:  # 记录头节点,，最小值节点
                self.head = cur
            self.pre = cur  # 保存 cur
            dfs(cur.right)  # 递归右子树

        if not root:
            return
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head


if __name__ == '__main__':
    a = arr_to_tree([4, 2, 5, 1, 3])
    a = Solution().treeToDoublyList(a)
    print(a)
