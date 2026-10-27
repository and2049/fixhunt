data = {'α', 'β'}
open('tmp.txt', 'w', encoding='utf-8').write(''.join(sorted(data)))
with open('tmp.txt', 'r', encoding='utf-8') as f:
    content = f.read()
import os; os.remove('tmp.txt')
print(repr(content))
