import time

from requests_html import HTMLSession
from lxml import etree


def func(num):
    for i in num:
        yield i


def func2(num):
    for i in num:
        print("返回值")
        return i


# f = func([1, 2, 3, 4, 5, 6, 7, 8])
f2 = func2([1, 2, 3, 4, 5, 6, 7, 8])
# for i in range(8):
#     print(next(f))

for i in range(8):
    print(f2)