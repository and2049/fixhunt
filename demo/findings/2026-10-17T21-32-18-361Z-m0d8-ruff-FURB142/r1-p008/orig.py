ref = []
def log_and_return(x):
    ref.append(x)
    return x * 2

s = set()
for i in range(3):
    s.add(log_and_return(i))
print('log:', ref)
print('set:', sorted(s))
