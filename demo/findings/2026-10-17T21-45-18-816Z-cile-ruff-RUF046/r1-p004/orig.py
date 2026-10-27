class FloatRound:
    def __round__(self, ndigits=0):
        return 3.14

z = FloatRound()
v = int(round(z))
print('int(round(z)):', v, type(v))
# After fix: round(z) -> 3.14 (float)
# So we simulate by showing what round(z) gives
print('round(z):', round(z), type(round(z)))
