class C:
    _val = 0
    @property
    def score(self):
        C._val += 1
        return C._val
    score = staticmethod(score)  # rule triggers: replaces property with staticmethod

c = C()
try:
    print(c.score)
except Exception as e:
    print(type(e).__name__, str(e))
