from django.test import TestCase

# Create your tests here.

d = {"name": "summer", "age":23, "sex": "male"}
# del d["name"]
# d.pop("name")
# d.popitem()
# print(d)

from threading import Timer
import time


def hello():
    print("hello, world")

for i in range(10):
    time.sleep(1)
    t = Timer(1, hello)
    t.start()



