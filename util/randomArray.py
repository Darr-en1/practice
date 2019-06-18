import random


def random_array(length, range_left, range_right):
    assert length >= 0, (
        "the length cannot be negative"
    )

    assert range_left > 0 and range_right > 0, (
        "range_left and range_right should more than the 0"
    )

    assert range_left < range_right, (
        "range_left should less than range_right"
    )

    # 可以通过 np.random.randint()函数
    return [random.randint(int(range_left), int(range_right)) for _ in range(length)]


if __name__ == '__main__':
    print(random_array(-4, 10.5, 3))
