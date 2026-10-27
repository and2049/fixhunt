str = lambda s: s.upper()  # shadow built-in str
class T:
    def __init__(self):
        self.str = 'hello'
t = T()
try:
    delattr(t, 'str')
    print('t.str after del:', t.str)
except Exception as e:
    print(f'{type(e).__name__}: {e}')
finally:
    del str  # restore built-in if needed
print('Built-in str still works:', str('test'))
