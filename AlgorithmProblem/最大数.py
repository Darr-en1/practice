from util.randomArray import random_array
from util.timeDecorator import time_decorator

__author__ = 'Darr_en1'

# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
import re



@time_decorator
def largest_number(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if int(str(nums[j]) + str(nums[j + 1])) < int(str(nums[j + 1]) + str(nums[j])):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return re.sub("^0+", "0", "".join([str(val) for val in nums]))


if __name__ == '__main__':
    res = largest_number(random_array(5, 3, 100))
    print(res)

    re2 = largest_number([0, 0])
    print(re2)
