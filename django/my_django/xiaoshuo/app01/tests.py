from django.test import TestCase

# Create your tests here.
from functools import reduce


res = reduce(lambda x,y:x+y,range(1,101))
print(res)