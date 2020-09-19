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
