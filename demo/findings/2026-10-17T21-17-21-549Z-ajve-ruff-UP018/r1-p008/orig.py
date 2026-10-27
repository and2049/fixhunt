import traceback
def g():
    return complex(1+2j)
def f():
    return g()
try:
    raise ValueError
except:
    tb = traceback.format_exc()
    print('complex' in tb)
