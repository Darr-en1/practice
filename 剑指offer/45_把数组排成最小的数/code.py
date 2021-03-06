from functools import cmp_to_key
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def sort_rule(x, y):  # 比较两个数字组成的新的数字大小
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        rep_str = [str(num) for num in nums]
        rep_str.sort(key=cmp_to_key(sort_rule))
        return "".join(rep_str)


print(Solution().minNumber([3, 30, 34, 5, 9]))
print(Solution().minNumber([128,12]))
