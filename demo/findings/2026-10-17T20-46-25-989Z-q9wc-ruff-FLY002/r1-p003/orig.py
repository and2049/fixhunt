class NotStr:
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return f'[{self.val}]'
    def __format__(self, fmt):
        return f'<{self.val}>'
a = NotStr('x')
b = NotStr('y')
try:
    res = ''.join((a, b))
except Exception as e:
    res = f'{type(e).__name__}: {e}'
try:
    fres = f'{a}{b}'
except Exception as e:
    fres = f'{type(e).__name__}: {e}'
print(f'join:{res}|fstring:{fres}')
