def f():
    b = b'hello\nworld'
    if b'
' in b:
        return None
    return b

result = f()
print(result is None)
