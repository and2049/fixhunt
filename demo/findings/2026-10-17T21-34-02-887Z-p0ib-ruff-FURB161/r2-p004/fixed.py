side = []
def f():
    side.append('f')
    return 3
def g():
    side.append('g')
    return 5
side.clear()
result = f() + bin(g()).count('1')
print(f'f then g: side={side}, result={result}')
side.clear()
result = bin(f()).count('1') + g()
print(f'bin(f) then g: side={side}, result={result}')
side.clear()
result = f() + bin(g()).bit_count()
print(f'f then bit_count g: side={side}, result={result}')
side.clear()
result = bin(f()).bit_count() + g()
print(f'bit_count f then g: side={side}, result={result}')
