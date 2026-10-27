def f(x=None):
    if x is None:
        x = {}
    if not hasattr(f, 'counter'):
        f.counter = 0
    f.counter += 1
    x['key'] = f.counter
    return x
class A(dict):
    pass
# Use class in default arg
call_log = []
def g(val=A()):  # mutable default: class instance
    call_log.append(val.copy())
    return val
g()
g()
g()
print('call log lengths:', [len(d) for d in call_log])
print('call log contents:', call_log)
