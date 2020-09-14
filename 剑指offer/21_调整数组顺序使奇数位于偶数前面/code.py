from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums) - 1
        while i < n:
            if not nums[i] % 2:
                nums[i], nums[n] = nums[n], nums[i]
                n -= 1
            else:
                i += 1
        return nums

    def exchange1(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums) - 1
        while i < n:
            while nums[i] % 2 and i < n:
                i += 1
            while not nums[n] % 2 and i < n:
                n -= 1
            nums[i], nums[n] = nums[n], nums[i]

        return nums
