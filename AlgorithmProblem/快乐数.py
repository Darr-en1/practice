class Solution:
    def isHappy(self, n: int) -> bool:
        b = []  # 用于判断是否进入循环
        while n not in b:
            b.append(n)
            n = sum(map(lambda x: int(x) ** 2, str(n)))
        return n == 1


if __name__ == '__main__':
    print(Solution().isHappy(7))
