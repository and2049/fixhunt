class FloatRound:
    def __round__(self, ndigits):
        return 3.5

z = FloatRound()
print(int(round(z)), type(int(round(z))))
print(round(z), type(round(z)))
