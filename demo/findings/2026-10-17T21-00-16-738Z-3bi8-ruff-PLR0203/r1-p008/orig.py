class C:
    default = []
    def append_val(x, *, lst=default):
        lst.append(x)
        return lst
    append_val = staticmethod(append_val)

print(C.append_val(1))
print(C.append_val(2))
