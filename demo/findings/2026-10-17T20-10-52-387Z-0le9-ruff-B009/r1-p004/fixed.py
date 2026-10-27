class UnicodeAttr:
    def __getattr__(self, name):
        if name == 'ſ':  # U+017F LATIN SMALL LETTER LONG S
            return 'long_s_value'
        raise AttributeError(name)

u = UnicodeAttr()
print(getattr(u, 'ſ'))
try:
    print(u.ſ)  # SyntaxError: invalid character
except SyntaxError as e:
    print('Dot access failed:', type(e).__name__)
