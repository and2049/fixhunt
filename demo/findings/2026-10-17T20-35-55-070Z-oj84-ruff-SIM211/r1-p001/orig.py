class MyBool(int):
    def __new__(cls, val):
        return super().__new__(cls, val)
    def __bool__(self):
        return bool(super().__int__())
    def __inv__(self):
        # Custom bitwise inversion that differs from logical negation
        return MyBool(~int(self))

obj = MyBool(1)  # truthy
# Original: False if obj else True -> evaluates to False
original = False if obj else True
# Ruff would rewrite as: not obj
rewritten = not obj
print(f'Original: {original}, Rewritten: {rewritten}')
assert original == rewritten, 'Should be equivalent'
