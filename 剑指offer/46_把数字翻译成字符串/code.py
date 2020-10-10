class Solution:
    def translateNum(self, num: int) -> int:
        re_str = str(num)
        a = 0

        def inner(idx):
            if idx >= len(re_str) - 1:
                nonlocal a
                a += 1
                return
            inner(idx + 1)
            if "10" <= re_str[idx:idx + 2] < "26":
                inner(idx + 2)

        inner(0)
        return a


print(Solution().translateNum(1068385902))
