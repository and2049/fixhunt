def gen():
    yield 'x'
    yield 'y'
g = gen()
first = ''.join(g)
try:
    second = ''.join(g)
except:
    second = '<exhausted>'
# Reset
g = gen()
fstring_first = f'{next(g)}{next(g)}'
print(f'join1:{first}|join2:{second}|fstring:{fstring_first}')
