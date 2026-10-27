def side():
    print('side effect')
    return []

x = side()
y = side()
print('Step 1 done')
result = not x is y
print('Result:', result)
