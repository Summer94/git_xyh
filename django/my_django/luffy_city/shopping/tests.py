from django.test import TestCase

# Create your tests here.

from multiprocessing import Process
import time

# def foo():
#     print(123)
#     time.sleep(1)
#     print('end foo')
#
# def bar():
#     print(456)
#     time.sleep(3)
#     print('end bar')
#
# if __name__ == '__main__':
#     p1 = Process(target=foo)
#     p2 = Process(target=bar)
#
#     p1.daemon = True
#
#     p1.start()
#     p2.start()
#     time.sleep(0.5)
#     print('主程序全部代码执行完毕')
