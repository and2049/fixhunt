import os

with open('test.txt', 'w', encoding='latin-1') as f:
    f.write('h\xe9llo')  # 'héllo' in latin-1

# Rule fires on: open('test.txt') in expression below
try:
    data = open('test.txt').read()  # rule adds encoding='utf-8' here
    print('Data (rule-affected):', repr(data))
except UnicodeDecodeError as e:
    print('UnicodeDecodeError:', e)

# Without fix (or correct encoding)
with open('test.txt', 'r', encoding='latin-1') as f:
    print('Correct:', repr(f.read()))

os.remove('test.txt')
