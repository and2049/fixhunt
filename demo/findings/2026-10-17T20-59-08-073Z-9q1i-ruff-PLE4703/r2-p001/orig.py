data = b'hello world'
s = {ord(c) for c in data.decode()}
for x in s:
    try:
        s.add(len(data))
    except RuntimeError as e:
        print('RuntimeError:', type(e).__name__, str(e))
print('final s:', sorted(s))
