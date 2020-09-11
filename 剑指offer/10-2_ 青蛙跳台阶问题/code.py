from functools import lru_cache


class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, b + a
        return a

    @lru_cache()
    def numWays1(self, n: int) -> int:
        if n < 2:
            return 1
        return self.numWays1(n - 1) + self.numWays1(n - 2)
