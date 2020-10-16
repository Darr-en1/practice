from typing import List
from collections import deque


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        t = deque([1, 2])
        _all = []
        sums = 3
        while len(t) > 1 and target > 2:
            if sums < target:
                sums += t[-1] + 1
                t.append(t[-1] + 1)
            elif sums > target:
                sums -= t.popleft()
            else:
                _all.append(list(t))
                sums -= t.popleft()
        return _all

print(Solution().findContinuousSequence(9))