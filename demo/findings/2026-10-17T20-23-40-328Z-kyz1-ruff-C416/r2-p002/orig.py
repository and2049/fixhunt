items = [(1, 'a'), (2, 'b')]
def get_items():
    print('get_items called')
    return items
# Rule fires here: rewrites {y: z for y, z in get_items()} to dict(get_items())
def f(d={y: z for y, z in get_items()}):
    print('f called')
    return d
print('Before first call:')
r1 = f()
items.append((3, 'c'))
print('After modifying items:')
r2 = f()
print(f'First result:  {r1}')
print(f'Second result: {r2}')
