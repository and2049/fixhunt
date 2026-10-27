flag = True
class C:
    def m(cls):
        return 'ok'
    if flag:
        m = classmethod(m)
print(type(C.m))
