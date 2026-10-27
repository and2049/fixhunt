def log(msg, *, file=None):
    if file:
        file.write(msg + '\n')
    return msg
f = open('tmp.txt', 'w')
try:
    x = 1
    assert x > 0, log('hello', file=f)
finally:
    f.close()
with open('tmp.txt') as f:
    print('file content:', f.read().strip())
