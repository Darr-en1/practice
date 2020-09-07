import random


def duplicate(nums):
    i = 0
    while i < len(nums):
        val = nums[i]
        if i == val:
            i += 1
        elif nums[i] == nums[val]:
            return val
        else:
            nums[i], nums[val] = nums[val], nums[i]


def random_list(length, repeat=False):
    if repeat:
        return [random.randint(0, length - 2) for _ in range(length)]
    else:
        res = [i for i in range(length)]
        random.shuffle(res)
        return res
