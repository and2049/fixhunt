def f(x):
    return open('temp.txt', 'a').write(x)
files = ['data1\n', 'data2\n']
sources = [b'hello', b'world']
try:
    list(map(f, sources))
except Exception as e:
    print(type(e).__name__, str(e))
finally:
    with open('temp.txt', 'r') as fp:
        print(fp.read(), end='')
