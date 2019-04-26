__author__ = 'Darr_en1'

# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
import re

class Solution:
    def largestNumber(self, nums):
        n = len(nums)
        for i in range(n - 1):
            for j in range(0, n - 1 - i):
                if int(str(nums[j]) + str(nums[j+1])) < int(str(nums[j+1]) + str(nums[j])):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return re.sub("^0+","0","".join([str(val) for val in nums]))



if __name__ == '__main__':
    res = Solution().largestNumber([3,30,34,5,9])
    re2 = Solution().largestNumber([0,0])
    print(res)
    print(re2)

