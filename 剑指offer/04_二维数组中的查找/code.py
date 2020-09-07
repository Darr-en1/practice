from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix:
            a = 0
            b = len(matrix[a]) - 1
            while a < len(matrix) and b >= 0:
                if matrix[a][b] > target:
                    b -= 1
                elif matrix[a][b] < target:
                    a += 1
                else:
                    return True
        return False


