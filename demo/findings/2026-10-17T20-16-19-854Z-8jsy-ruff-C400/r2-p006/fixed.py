with open('test.txt', 'w') as f:
    for item in list(str(x) for x in [1, 2, 3]):
        f.write(item)
with open('test.txt', 'r') as f:
    print(f.read())
