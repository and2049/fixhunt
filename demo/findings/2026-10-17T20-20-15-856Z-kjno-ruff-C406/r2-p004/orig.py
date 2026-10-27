with open('test.txt', 'w') as f:
    data = [(b'hello', 5)]
    d = dict(data)
    try:
        f.write(str(d))  # This will work
    except Exception as e:
        print(type(e).__name__, str(e))
with open('test.txt', 'r') as f:
    print(f.read())
