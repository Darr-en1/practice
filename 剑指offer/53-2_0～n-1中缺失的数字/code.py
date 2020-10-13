from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def check(tar):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] > tar:
                    end = mid - 1
                else:
                    start = mid + 1

            return start

        return check(target) - check(target - 1)


print(Solution().search([5, 7, 7, 8, 8, 10], target=10))
