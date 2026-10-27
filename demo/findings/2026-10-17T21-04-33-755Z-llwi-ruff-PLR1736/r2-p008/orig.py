class Foo:
    def __init__(self, n):
        self.n = n
    def __str__(self):
        print(f'str({self.n})')
        return f'str_{self.n}'
    def __repr__(self):
        print(f'repr({self.n})')
        return f'repr_{self.n}'

lst = [Foo(1), Foo(2)]
for i, x in enumerate(lst):
    s = f'{lst[i]}'  # rule fires: lst[i] -> x
print('line')
for i, x in enumerate(lst):
    s = str(lst[i])  # rule fires again
print('done')
