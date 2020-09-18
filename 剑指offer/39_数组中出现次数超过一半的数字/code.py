from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        exist = defaultdict(int)
        l = len(nums) // 2
        for i in nums:
            exist[i] += 1
            if exist[i] > l:
                return i
