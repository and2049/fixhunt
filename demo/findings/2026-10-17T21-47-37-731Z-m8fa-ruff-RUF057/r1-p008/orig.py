def h(x=[]):
    x.append(1)
    return len(x)
a = round(h(), 0)
b = round(h(), 0)
print('a:', a, 'b:', b)
# After fix: h() still called twice, each time mutates default list
