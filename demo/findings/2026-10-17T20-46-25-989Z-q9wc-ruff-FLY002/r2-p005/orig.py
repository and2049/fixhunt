sep = '{name}'
a = 'Alice'
b = 'Bob'
joined = sep.join((a, b))
print(repr(joined))  # 'Alice{name}Bob'
# F-string would try: f'Alice{name}Bob' -> NameError if name undefined, or value if defined
# To make deterministic: define name
name = 'X'
fstring_result = f'{a}{sep}{b}'
print(f'F-string gives: {repr(fstring_result)}')  # 'Alice{X}Bob' != 'Alice{name}Bob'
