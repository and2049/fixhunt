from datetime import datetime

def f():
    class X:
        def __init__(self, v):
            self.v = v
        def __bool__(self):
            return self.v != ''
        def __len__(self):
            return len(self.v)
    s = X('2023-01-01T12:00:00Z')
    t = datetime.fromisoformat(s.replace("Z", "+00:00"))
    u = datetime.fromisoformat(str(s))
    print('t:', t.isoformat())
    print('u:', u.isoformat())
    print('equal?', t == u)
    print('same?', t is u)
f()
