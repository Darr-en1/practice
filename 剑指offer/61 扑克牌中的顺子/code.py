from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        a = set()
        _max = _min = 0, 14
        for n in nums:
            if n in a:
                return False
            if n != 0:
                a.add(n)
                _min = min(n, _min)
                _max = max(n, _max)
        if _max - _min > len(nums) - 1:
            return False
        return True
