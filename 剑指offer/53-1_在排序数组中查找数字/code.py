from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == mid:
                start = mid + 1
            else:
                end = mid - 1
        return start