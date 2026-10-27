with open('test.txt', 'w') as f:
    f.write('hello')  # noqa: FAKE
with open('test.txt', 'r') as f:
    print(f.read())
