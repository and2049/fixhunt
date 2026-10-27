with open('test.txt', 'w') as f:
    if not '' != '':
        f.write('hello')
with open('test.txt', 'r') as f:
    print(f.read())
