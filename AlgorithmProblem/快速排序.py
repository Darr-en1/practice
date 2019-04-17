__author__ = 'Darr_en1'




def quick_sort(list,low,high):
    """
    :param list:排序对象
    :param low: 起始位索引
    :param high: 终止位索引
    :return: 排序后的list

    思路：
    quick_sort会确定key 在 list中排序后的索引，通过分而治之的方案，
    将大于key和小于key,分别放置在其两侧，然后递归排序。

    时间复杂度：Ο(n log n)
    空间复杂度：Θ(lgn)


    """
    if low > high:
        return list

    _low = low
    _high = high
    key = list[_low]

    while low < high:
        while low < high and list[high] >= key:
            high -=1


        while low < high and list[low] <= key:

            low +=1

        if low < high:
            list[high],list[low] = list[low],list[high]

    list[low],list[_low] = key,list[low]

    quick_sort(list,_low,low-1)
    quick_sort(list,high+1,_high)

    return list



if __name__ == '__main__':
    print(quick_sort([3,6,8,2,9,4,10],0,6))
