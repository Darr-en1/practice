from typing import List
from collections import deque


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, j, res, _all = 1, 2, 3, []
        while i < j:
            if res == target:
                _all.append(list(range(i, j + 1)))
            if res >= target:
                res -= i
                i += 1
            else:
                j += 1
                res += 1
        return _all


print(Solution().findContinuousSequence(9))
