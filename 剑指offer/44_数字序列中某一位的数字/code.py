from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        rep_str = list(map(lambda x: str(x), nums))
        rep_str.sort(key=lambda x: x)
        return "".join(rep_str)


print(Solution().minNumber([10, 2]))

print("3" > "30")