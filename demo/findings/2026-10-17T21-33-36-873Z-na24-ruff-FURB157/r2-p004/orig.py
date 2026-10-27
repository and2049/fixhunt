data = b'hello\nworld'
try:
    # Rule does not fire on bytes, but if someone mistakenly uses str on int thinking it's bytes
    num = 42
    s = str(num)  # '42' as str
    b = s.encode()  # b'42'
    print('str then encode:', b)
    # If fix removes str: s = num -> int, then .encode() fails
    # Simulate risk: function expects str
    def needs_str(x):
        return x.encode()
    print('needs_str(str(42)):', needs_str(str(42)))
except AttributeError as e:
    print('AttributeError:', e)
