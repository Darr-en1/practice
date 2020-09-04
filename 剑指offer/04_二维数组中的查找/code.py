import random


def find(arr,num):
    if not arr:
        return False

    for index, value in enumerate(arr):
        for idx, val in enumerate(value):
            if val > num:

            if nums[in dex] == nums[value]:
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
