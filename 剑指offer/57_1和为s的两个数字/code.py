from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = set()
        for n in nums:
            if n not in a:
                a.add(target - n)
            else:
                return [n, target - n]

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while nums[i] + nums[j] != target:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        return [nums[i], nums[j]]


print(Solution().twoSum1([2, 7, 11, 15] , 9))
