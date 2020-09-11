from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        """:raise
        常规
        """
        i, j = 0, 1
        while i < len(numbers) - 1:
            if numbers[i] <= numbers[j]:
                i += 1
                j += 1
            else:
                return numbers[j]
        return numbers[0]

    def minArray2(self, numbers: List[int]) -> int:
        """:raise
        二分查找
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                j -= 1
        return numbers[i]


a = Solution().minArray([1, 3, 5])
print(a)
