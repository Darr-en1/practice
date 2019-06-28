class Solution:
    def singleNumber(self, nums):
        """
        数学运算
        时间复杂度： O(n)
         空间复杂度：O(n)
        """
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber2(self, nums: list) -> int:
        """
         异或思路
         时间复杂度： O(n)
         空间复杂度：O(1)
         """
        a = 0
        for i in nums:
            a ^= i
        return a
