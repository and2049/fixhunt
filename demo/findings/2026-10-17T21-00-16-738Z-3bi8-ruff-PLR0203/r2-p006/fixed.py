def make_class():
    x = 10
    class C:
        @staticmethod
        def get():
            nonlocal x
            return x
    return C
C = make_class()
print(C().get())
