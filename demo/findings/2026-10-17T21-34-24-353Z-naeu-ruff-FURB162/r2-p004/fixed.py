from datetime import datetime
class MockStr:
    def __init__(self, s):
        self.s = s
    def replace(self, a, b):
        print('replace called')
        return self.s.replace(a, b)
    def __bool__(self):
        return len(self.s) > 10
    def __len__(self):
        return len(self.s)
s = MockStr('2024-01-01T00:00:00Z')
print('bool(s):', bool(s))
if s:  # uses __bool__
    dt = datetime.fromisoformat(s.replace('Z', '+00:00'))  # rule fires here
    print('parsed:', dt)
else:
    print('false branch')
