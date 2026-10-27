calls = []
def f():
    calls.append(len(calls))
    return len(calls) < 2
x = f() and not f()
print('result:', x, 'calls:', calls)
