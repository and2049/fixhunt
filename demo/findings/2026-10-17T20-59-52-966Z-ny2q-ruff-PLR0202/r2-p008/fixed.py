class C:
    @classmethod
    def m(cls, lst=[]):
        lst.append(1)
        return lst
print(C.m())
print(C.m())
