with open('test.txt', 'w') as f:
    f.write = lambda data: f.__write__(data.upper())
    f.write('hi')
with open('test.txt') as f:
    print(f.read())
import os; os.remove('test.txt')
