class C:
    def m(cls):
        return b'data'
    m = classmethod(m)
with open('tmp.bin', 'wb') as f:
    f.write(C.m())
with open('tmp.bin', 'rb') as f:
    print(f.read())
import os; os.remove('tmp.bin')
