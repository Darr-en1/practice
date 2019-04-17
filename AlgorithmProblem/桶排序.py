__author__ = 'Darr_en1'

def bucket_sort(array):
    """
    桶排序：就是定义一个数组，每个索引位置定义一个大小的区间，
    待排序数组遍历并写入到指定区间（可以通过在该索引外接数组或则链表），
    区间内部也进行排序（类似插入排序），
    遍历完成后对数组及数组中的区间数组进行遍历，得到排序数组
    
    
    
    这里的桶排的写法是利用创建一个长度为输入数组array最大值的临时数组book,
    然后把array中的值逐一代入book的索引，对应的book数组索引下的值就是数字出现的次数，
    从而返回book中的非零索引即可


    :param array:
    :return:
    """
    if not array:
        return False
    max_len = max(array)+1
    book = [0 for _ in range(0,max_len)]#定义和最大数值等长的数组
    for i in array:
        book[i] += 1
    # 遍历取得排序数组，索引对应值，对应的值表示个数
    return [i for i in range(0,max_len) for _ in range(0,book[i])]


if __name__ == '__main__':
    print(bucket_sort([6,3,5,9,2,10,7]))
