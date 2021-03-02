from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = float("-inf")
        curr = 0
        for i in nums:

            if curr < 0 or curr + i < 0:
                curr = i
            else:
                curr += i
            if curr > m:
                m = curr
        return m

    def maxSubArray1(self, nums: List[int]) -> int:
        _max = float('-inf')
        curr = 0
        for n in nums:
            curr = max(curr + n, n)
            _max = max(_max, curr)
        return _max
