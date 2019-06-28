from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0
        for n in nums:
            if n:
                nums[curr] = n
                curr += 1
        _rep = nums[curr:]
        nums[curr:] = [0 for _ in _rep]
        print(nums)


if __name__ == '__main__':
    a = [0, 1, 0, 3, 12, 0, 10, 11, 0, 0]
    print(Solution().moveZeroes(a))
