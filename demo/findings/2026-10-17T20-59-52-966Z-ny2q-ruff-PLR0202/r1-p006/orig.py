class C:
    def m(cls): return b'hello'
    m = classmethod(m)

with open('test.bin', 'wb') as f:
    for i in range(2):
        f.write(m())  # writes b'hello' twice

with open('test.bin', 'rb') as f:
    print('file contents:', f.read())
import os; os.remove('test.bin')
