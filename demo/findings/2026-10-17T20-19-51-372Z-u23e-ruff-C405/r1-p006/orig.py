data = [b'hello\n', b'world\n']
trace = []
class TrackedBytes(bytes):
    def __new__(cls, b): trace.append(b); return super().__new__(cls, b)
s = set(TrackedBytes(b) for b in data)
print(''.join(trace), sorted(s))
