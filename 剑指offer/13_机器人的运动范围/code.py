class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        exist = set()

        def dfs(a, b):

            if not 0 <= a < m or not 0 <= b < n or f"{a},{b}" in exist or parse(a) + parse(b) > k:
                return
            exist.add(f"{a},{b}")
            dfs(a + 1, b)
            dfs(a, b + 1)

        def parse(num):
            res = 0
            while num != 0:
                res += num % 10
                num = num // 10
            return res

        dfs(0, 0)
        return len(exist)


if __name__ == '__main__':
    print(Solution().movingCount(3, 1, 0))
