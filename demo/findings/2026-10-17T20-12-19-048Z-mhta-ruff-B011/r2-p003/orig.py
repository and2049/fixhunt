f = lambda: assert False or 1
try:
    result = f()
    print('result:', result)
except SyntaxError as e:
    print('SyntaxError:', e.msg)
