class NumAttr:
    def __getattr__(self, name):
        if name == '123':
            return 'numeric_attr'
        raise AttributeError(name)

n = NumAttr()
print(getattr(n, '123'))
try:
    print(n.123)  # Invalid syntax
    print('Dot access succeeded')
except SyntaxError as e:
    print('Dot access failed:', type(e).__name__)
