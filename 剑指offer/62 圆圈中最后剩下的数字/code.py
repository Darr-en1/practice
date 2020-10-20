class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        a = list(range(n))
        h = m
        while len(a) > 1:
            idx = (h - 1) % n
            a.pop(idx)
            n -= 1
            h = idx + m
        return a[0]


print(Solution().lastRemaining(5, 3))
