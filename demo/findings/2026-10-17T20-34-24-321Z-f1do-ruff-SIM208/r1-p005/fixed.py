calls = []

def get_val():
    calls.append(len(calls))
    return len(calls) % 2 == 0

def f(arg):
    return arg, len(calls)

out = f(bool(get_val()))
print('result:', out)
calls.clear()
out2 = f(get_val())
print('after fix simulation:', out2)
