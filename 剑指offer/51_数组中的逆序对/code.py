import copy
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(left, mid, right):
            count = 0
            for i in range(left, right + 1):
                temp[i] = nums[i]
            i = k = left
            j = mid + 1
            while left <= i <= mid < j <= right:
                if temp[i] <= temp[j]:

                    nums[k] = temp[i]
                    i += 1
                else:
                    count += mid - i + 1
                    nums[k] = temp[j]
                    j += 1
                k += 1

            while i <= mid:
                nums[k] = temp[i]
                k += 1
                i += 1

            while j <= right:
                nums[k] = temp[j]
                k += 1
                j += 1

            return count

        def sort(left, right):
            if left < right:
                mid = left + (right - left) // 2
                c = sort(left, mid) + sort(mid + 1, right)
                if nums[mid] <= nums[mid + 1]:
                    # 此时不用计算横跨两个区间的逆序对，直接返回 reverse_pairs
                    return c
                return c + merge(left, mid, right)
            return 0

        temp = copy.copy(nums)
        return sort(0, len(nums) - 1)


print(Solution().reversePairs([2, 4, 3, 5, 1]))
