f = lambda: True and False or True
result = f() and print('inner') or print('outer')
f = lambda: (True and False) or True
result = f() and print('inner') or print('outer')
