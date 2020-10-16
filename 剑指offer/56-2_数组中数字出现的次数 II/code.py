from typing import List
from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = defaultdict(int)
        for n in nums:
            a[n] += 1
            if a[n] > 2:
                a.pop(n)
        return list(a.keys()).pop()


print(Solution().singleNumber([3, 4, 3, 3]))
