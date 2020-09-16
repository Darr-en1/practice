from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        # 需要一个先进先出的队列和一个保存信息的集合
        if not root:
            return []
        queue, res = deque(), []
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):  # 需要注意queue会不断变化，需要记录当时的长度
                node = queue.popleft()
                if node:
                    tmp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if tmp:
                res.append(tmp)
        return res
