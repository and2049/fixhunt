class MyStr(str):
    def __new__(cls, s):
        return super().__new__(cls, s)

s = MyStr(b'hello'.decode())
print(type(s))
print(repr(s))
