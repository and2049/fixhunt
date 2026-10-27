s = '0b10'
with open('test.txt', 'w') as f:
    f.write(str(int(s[2:], 2)))
with open('test.txt', 'r') as f:
    print(f.read())
