import math
original_len = len
def f():
    global len
    global sum
    len = lambda x: 99
    sum = lambda x: 88
    return len([1,2,3]) + sum([4,5])
print(f())
print('len overridden:', len == (lambda x: 99))
print('sum overridden:', sum == (lambda x: 88))
print('math.len unchanged:', math.len is original_len)
