class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # 数字的交集(对其二进制最后一位的交集比较)
            res += n & 1
            n = n >> 1
        return res
