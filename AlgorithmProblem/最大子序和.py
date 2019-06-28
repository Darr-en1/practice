class Solution:
    def maxSubArray(self, nums: list) -> int:
        minus_nums = 0
        now = 0
        res = 0
        for index, num in enumerate(nums):
            if now > 0: num
            now += num
            if num > 0:
                now = index
                if minus_nums + res > num:
                    res += minus_nums + num
                    minus_nums = 0
            else:
                if now > 0:
                    minus_nums += num

        return res


if __name__ == '__main__':
    a = Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
