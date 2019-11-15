from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)

        while start != end and nums[start] == min(nums[start:end]):
            start += 1

        while start != end and nums[end - 1] == max(nums[start:end]):
            end -= 1

        return end - start

    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)

        while self.compare_start(nums, start, end):
            start += 1

        while self.compare_end(nums, start, end):
            end -= 1

        return end - start

    def compare_start(self, nums, start, end):
        if start == end:
            return False

        for i in range(start + 1, end):
            if nums[start] > nums[i]:
                return False
        return True

    def compare_end(self, nums, start, end):
        if start == end:
            return False

        for i in range(start, end - 1):
            if nums[end - 1] < nums[i]:
                return False
        return True


if __name__ == '__main__':
    a = [2, 3, 4, 3, 8, 10, 12, 15]
    # for i in range(7, 8):
    #     print(i)
    print(Solution().findUnsortedSubarray1(a))
