def call_split(*args):
    s = 'x y z'
    return s.split(*args)[0]  # rule sees split(*args)[0]
try:
    print(call_split())          # -> 'x'
    print(call_split(' ', 1))    # -> split(' ', 1, 1) -> TypeError
    print(call_split(maxsplit=1))# -> split(None, maxsplit=1, maxsplit=1) -> TypeError
except TypeError as e:
    print('TypeError:', e)
