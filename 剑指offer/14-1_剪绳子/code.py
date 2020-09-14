import functools

import math


class Solution:

    @functools.lru_cache()
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        res = -1
        for i in range(1, n):
            res = max(res, max(i * self.cuttingRope(n - i), i * (n - i)))
        return res

    def cuttingRope1(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                tmp = max(j, dp[j]) * max(i - j, dp[i - j])
                dp[i] = max(dp[i], tmp)
        return dp[-1]

    def cuttingRope2(self, n: int) -> int:
        """
        通过数学计算得到的结论
        :param n:
        :return:
        """
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        if b == 1:
            return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)


if __name__ == '__main__':
    Solution().cuttingRope(5)
