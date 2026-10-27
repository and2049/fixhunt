def g():
    print('executed')
    return 1
x = g()
y = never_defined if False else 3
val = x and [] and y
print('val:', val)
