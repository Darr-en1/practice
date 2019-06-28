from typing import List


class Solution:
    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))

    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n + 1):
            if i not in nums:
                nums.append(i)
        return nums[n:]

    def findDisappearedNumbers3(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        c = []
        for i in range(1, n + 1):
            if i not in nums:
                c.append(i)
        return c


if __name__ == '__main__':
    print(Solution().findDisappearedNumbers1([4, 3, 2, 7, 8, 2, 3, 1]))
