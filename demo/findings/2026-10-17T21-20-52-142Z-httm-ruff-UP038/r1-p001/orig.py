class FalsyInt(int):
    def __bool__(self): return False

class TruthyStr(str):
    def __bool__(self): return True

x = FalsyInt(5)
y = TruthyStr('')
print(isinstance(x, (int, str)), isinstance(y, (int, str)))
