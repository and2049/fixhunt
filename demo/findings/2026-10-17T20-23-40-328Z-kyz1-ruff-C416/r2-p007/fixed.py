items = [('a', 1)]
# Rule fires here in default arg: rewrites {k: v for k, v in items} to dict(items)
def process(*, mapping={k: v for k, v in items}):
    print('process called')
    return mapping.copy()
print('First call:')
r1 = process()
items.append(('b', 2))
print('Second call (after modifying items):')
r2 = process()
print(f'First result:  {r1}')
print(f'Second result: {r2}')
print(f'Same object?   {r1 is r2}')
