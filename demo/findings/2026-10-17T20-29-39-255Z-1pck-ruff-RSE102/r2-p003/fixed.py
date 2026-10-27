assigned = None
try:
    raise ((err := ValueError)())()
except ValueError as e:
    assigned = err
print('Assigned:', assigned is not None)
print('err is', err if assigned else 'None')
try:
    raise (err := ValueError)()
except ValueError as e:
    print('Second err:', err)
