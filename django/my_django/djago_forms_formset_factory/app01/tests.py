from django.test import TestCase

# Create your tests here.

l = [11, 2, 3, 11, 3, 7, 2]

# print(set(l))
# l2 = sorted(set(l), key=l.index)
# print(l2)

# def func(m):
#     print(m)
#     for k, v in m.items():
#         m[k + 2] = v + 2
#
# m = {1:2,3:4}
# print(1)
# l = m
# l[9] = 10
# print(2)
# func(l)
# print(3)
# m[7] = 8
# print(l)
# print(m)

# l = [1, 2, [3, [4, 5]], 6, [7, ]]
# l2 = []
#
# def func(l):
#     for i in l:
#         if isinstance(i, list):
#             func(i)
#         else:
#             l2.append(i)
#
# func(l)
# print(l2)





# def func(l):
#     print(l)
#     if isinstance(l,list):
#         return [y for x in l for y in func(x)]
#     else:
#         return [l]
#
# func(l)

# def func(n):
#     a = 1
#     for i in range(5):
#         c = yield a
#         a += 1
#
#
# f = func(22)
# for i in f:
#     print(i)

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count

a = averager()
next(a)
print(a.send(11))
print(a.send(100))