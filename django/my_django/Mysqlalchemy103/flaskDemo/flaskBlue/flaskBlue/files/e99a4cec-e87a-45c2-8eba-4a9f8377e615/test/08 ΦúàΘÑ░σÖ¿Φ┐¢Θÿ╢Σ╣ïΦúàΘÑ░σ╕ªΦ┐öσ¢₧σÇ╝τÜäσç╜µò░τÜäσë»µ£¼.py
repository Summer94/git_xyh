# 装饰带返回值的函数


def wrapper(func):
    def inner():
        print('开始')
        r = func()  # 拿到原来函数的返回值
        print(r)
        print('结束')
        return r
    return inner


@wrapper
def f1():
    print('我是f1')
    return 100


ret = f1()
# print(ret)

