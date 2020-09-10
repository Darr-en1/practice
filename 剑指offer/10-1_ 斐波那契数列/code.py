from functools import lru_cache


class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    @lru_cache()
    def fib1(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib1(n - 1) + self.fib1(n - 2)


print(Solution().fib1(5))
