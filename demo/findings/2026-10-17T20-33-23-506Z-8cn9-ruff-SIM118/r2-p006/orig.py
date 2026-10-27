def process(*, mapping={'a': 1}, /, **kw):
    mapping['b'] = 2
    return 'b' in mapping.keys()

print(process())
print(process())  # Second call sees mutated default
