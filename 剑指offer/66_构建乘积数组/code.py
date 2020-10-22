from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        b, tmp = [1] * len(a), 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]  # 下三角
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]  # 上三角
            b[i] *= tmp  # 下三角 * 上三角
        return b

print(list(range(10,-1,-1)))