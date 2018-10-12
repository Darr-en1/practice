
"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
"""


class Solution:

    def twoSum(self,nums, target):
        """
        时间复杂度：O(n)

        空间复杂度：O(n)
        """
        n = len(nums)
        d = {}
        for x in range(n):
            a = target - nums[x]
            if nums[x] in d:    #底层hash表实现 时间复杂度O(1)
                return d[nums[x]],x

            else:
                d[a] = x

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15],13))

