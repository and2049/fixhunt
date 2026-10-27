import sys

def f():
    d = {}  # baseline dict
    c = MyDict()  # user-defined dict-like
    print(type(d) is dict)
    print(type(c) is dict)

class MyDict(dict):
    pass

f()
