def f():
    print('side effect')
    return 'ok'
result = str(f())
print('result:', result)
