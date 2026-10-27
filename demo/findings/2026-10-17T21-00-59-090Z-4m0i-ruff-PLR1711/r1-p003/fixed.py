def w():
    data = b'hi'
    with open('tmp.bin', 'wb') as fp:
        n = fp.write(data)
n = w()
with open('tmp.bin', 'rb') as fp:
    print(fp.read())
import os; os.remove('tmp.bin')
