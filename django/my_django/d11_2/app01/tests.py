from django.test import TestCase

# Create your tests here.
from types import FunctionType,MethodType


import datetime
from functools import reduce

from functools import partial

class Foo(object):

    def __init__(self):
        self.request = "111"
        self.session = "session"

foo = Foo()

def func(args):
    return getattr(foo,args)

re_func = partial(func,'request')
se_func = partial(func,'session')

print(re_func())

# li = [6,2,3,4,5]
# s = reduce(lambda x,y:x+y,li)
# print(s)
# print(sum(li))
# a = range(3)
# print(type(a))

# print(datetime.datetime.now().strftime("%Y-%m-%d"))
#
# d = {"1":"asd", "2": "asd"}
# print(d.items())
# for i in d.items():
#     print(i)
#
# for k, v in enumerate(d):
#     print(k, v, d[v])
#
# print(d.keys())
# print(d.values())