class C:
    def m(cls, lst=[]):
        lst.append(1)
        return lst
    m = classmethod(m)
print(C.m())
print(C.m())
