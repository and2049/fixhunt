x = True
lam = lambda cond=(False if x else True): cond
print('lam():', lam())
import inspect
try:
    print('source:', inspect.getsource(lam))
except Exception as e:
    print('inspect failed:', type(e).__name__, str(e))
