def read_data(self=b''):
    data = self.decode() if isinstance(self, bytes) else self
    return len(data)

print(read_data(b'hello'))
try:
    print(read_data('world'))
except Exception as e:
    print(type(e).__name__, str(e))
