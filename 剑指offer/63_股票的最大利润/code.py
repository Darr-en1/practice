from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        _max = 0
        for p in prices[1:]:
            if p < start:
                start = p
            else:
                _max = max(p - start, _max)
        return _max

    def maxProfit1(self, prices: List[int]) -> int:
        start = float("+inf")
        _max = 0
        for p in prices:
            start = min(start, p)
            _max = max(p - start, _max)
        return _max
