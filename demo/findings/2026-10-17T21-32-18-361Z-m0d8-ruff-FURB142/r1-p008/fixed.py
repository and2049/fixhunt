ref = []
def log_and_return(x):
    ref.append(x)
    return x * 2

s = set()
s.update(log_and_return(i) for i in range(3))
print('log:', ref)
print('set:', sorted(s))
