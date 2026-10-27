def side():
    print('side effect')
    return []

x = side()
y = side()
print('Step 1 done')
result = x is not y
print('Result:', result)
