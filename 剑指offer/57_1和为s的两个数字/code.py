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
        a, b = 0, len(nums) - 1
        while a < b:
            s = nums[a] + nums[b]
            if a == target:
                return [nums[a], nums[b]]
            elif a > target:
                b -= 1
            else:
                a += 1


print(Solution().twoSum1([2, 7, 11, 15] , 9))
