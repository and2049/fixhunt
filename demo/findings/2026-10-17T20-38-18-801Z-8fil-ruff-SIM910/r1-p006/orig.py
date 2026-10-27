counter = 0
side_effect = lambda: nonlocal_counter := counter + 1 or exec('nonlocal_counter = 1')
# Actually, simpler: use a function that prints
def f():
    print('side effect')
    return 99

d = {}
# This would be dangerous if default had side effects, but we show the call shape
v = d.get('missing', None)  # Rule triggers
print(f'got: {v}')
