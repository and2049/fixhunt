class AlwaysFalse:
    def __bool__(self):
        return False
    def __repr__(self):
        return 'AlwaysFalse()'

obj = AlwaysFalse()
val = obj or 'fallback'
print('ternary:', val)
# After fix: val = obj or 'fallback'
val = obj or 'fallback'
print('or     :', val)
