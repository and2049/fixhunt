class Obj:
    def __init__(self):
        self.s = 'normalized'
        setattr(self, '\u017f', 'long_s')
obj = Obj()
print(getattr(obj, '\u017f'))
# After fix: obj.\u017f -> accesses obj.s due to NFKC normalization
