import os
def p(path: "str"):  # Rule may unquote to path: str
    return os.path.exists(path)
with open('tmp.txt', 'w') as f:
    f.write('test')
print('exists:', p('tmp.txt'))
os.remove('tmp.txt')
