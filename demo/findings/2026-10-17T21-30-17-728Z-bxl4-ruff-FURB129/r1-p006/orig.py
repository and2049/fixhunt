import os
os.remove('test.txt') if os.path.exists('test.txt') else None
with open('test.txt', 'w') as f:
    f.write('a\nb')
with open('test.txt', 'r') as fp:
    lines = fp.readlines()  # this is what we iterate over
    print('Type of lines:', type(lines).__name__)
    print('Is list?', isinstance(lines, list))
    lines.append('extra')  # only works on list
    for line in lines:
        print('Iterating:', line.strip())
    print('Length after append:', len(lines))
os.remove('test.txt')
