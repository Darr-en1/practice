"""
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        _len = len(nums)
        return (set(range(_len + 1)) - set(nums)).pop()

    def missingNumberOther(self, nums: List[int]) -> int:
        _len = len(nums)
        return sum(range(_len + 1)) - sum(nums)


if __name__ == '__main__':
    a = Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
    print(a)
