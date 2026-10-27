class C:
    default = []
    @staticmethod
    def append_val(x, *, lst=default):
        lst.append(x)
        return lst

print(C.append_val(1))
print(C.append_val(2))
