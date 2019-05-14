from util.randomArray import random_array

__author__ = 'Darr_en1'


def quick_sort(list_, low, high):
    """
    :param list_:排序对象
    :param low: 起始位索引
    :param high: 终止位索引
    :return: 排序后的list_

    思路：
    quick_sort会确定key 在 list_中排序后的索引，通过分而治之的方案，
    将大于key和小于key,分别放置在其两侧，然后递归排序。

    时间复杂度：Ο(n log n)
    空间复杂度：Θ(lgn)


    """
    if low > high:
        return list_

    _low = low
    _high = high
    key = list_[_low]

    while low < high:
        while low < high and list_[high] >= key:
            high -= 1

        while low < high and list_[low] <= key:
            low += 1

        if low < high:
            list_[high], list_[low] = list_[low], list_[high]

    list_[low], list_[_low] = key, list_[low]

    quick_sort(list_, _low, low - 1)
    quick_sort(list_, high + 1, _high)

    return list_


if __name__ == '__main__':
    print(quick_sort(random_array(10, 5, 25), 0, 9))
