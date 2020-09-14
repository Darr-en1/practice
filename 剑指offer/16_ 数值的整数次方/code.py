class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:  # 超时
            res *= x
            n -= 1
        return res

    def myPow1(self, x: float, n: int) -> float:
        if x == 0: return 0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            # 快速幂解析（二分法角度）
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res


print(Solution().myPow(2, 3))
