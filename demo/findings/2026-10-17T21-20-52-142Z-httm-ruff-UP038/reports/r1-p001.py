class TruthyStr(str):
    def __bool__(self): return True
