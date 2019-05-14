import time


# 可以通过类装饰器 通过__call__   可以带参数的装饰器 通过多一层的函数嵌套
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print(f"{func.__name__} 函数运行时间为 {stop_time - start_time}")

        return res

    return wrapper
