import random


def duplicate(nums):
    if not nums:
        return None

    for index, value in enumerate(nums):
        while index != value:
            if nums[index] == nums[value]:
                return value
            nums[index], nums[value] = nums[value], nums[index]
            value = nums[index]  # 获取交换后的value
    return None


def random_list(length, repeat=False):
    if repeat:
        return [random.randint(0, length - 2) for _ in range(length)]
    else:
        res = [i for i in range(length)]
        random.shuffle(res)
        return res


def test_exist_repeat():
    assert type(duplicate(random_list(length=10, repeat=True))) == int


def test_not_exist_repeat():
    assert duplicate(random_list(length=10)) is None
