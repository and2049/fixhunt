with open('test.bin', 'wb') as f:
    f.write(b'hello')  # noqa: SIM115
with open('test.bin', 'rb') as f:
    print(f.read())
import os; os.remove('test.bin')
