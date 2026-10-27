class Test:
    def __init__(self):
        self.i = 'dotless_i'
        self.\u0131 = 'Turkish_dotless_i'  # U+0131 LATIN SMALL LETTER DOTLESS I
t = Test()
# NFKC: \u0131 -> i (U+0069), so t.\u0131 becomes t.i
print(getattr(t, '\u0131'))  # Should print 'Turkish_dotless_i'
# After fix: t.\u0131 -> t.i -> 'dotless_i' (wrong)
