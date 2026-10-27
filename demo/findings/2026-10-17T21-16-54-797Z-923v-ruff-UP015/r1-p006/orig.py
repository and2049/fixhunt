name = b'file.txt'
with open(name, 'r') as f:  # trigger: name is bytes, but mode 'r' still valid in Py3
    print(type(f.read()))
import os; os.remove('file.txt')
