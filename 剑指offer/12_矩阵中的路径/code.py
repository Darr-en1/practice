from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):

            # 终止条件：
            # 返回 false ： ① 行或列索引越界 或 ② 当前矩阵元素与目标字符不同 或 ③ 当前矩阵元素已访问过 （③ 可合并至 ② ） 。
            # 返回 true ： 字符串 word 已全部匹配，即 k = len(word) - 1 。
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            tmp, board[i][j] = board[i][j], '/'
            res = dfs(i + 1, j, k + 1) or \
                  dfs(i - 1, j, k + 1) or \
                  dfs(i, j + 1, k + 1) or \
                  dfs(i, j - 1, k + 1)
            board[i][j] = tmp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False


if __name__ == '__main__':
    board = [
        ["a", "b", "c", "e"],
        ["s", "f", "c", "s"],
        ["a", "d", "e", "e"]
    ]
    word = "bfce"
    print(Solution().exist(board, word))
