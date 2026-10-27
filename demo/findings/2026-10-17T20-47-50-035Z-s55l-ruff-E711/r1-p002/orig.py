def expects_bool(b):
    return 'yes' if b else 'no'
x = None
result = expects_bool(x == None)
print(result)
