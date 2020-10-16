from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        a = set()
        for n in nums:
            if n in a:
                a.remove(n)
            else:
                a.add(n)
        return list(a)
