fns = []
for i in range(2):
    if i == 0:
        fns.append(lambda: (err := ValueError(i)))
    else:
        fns.append(lambda: err)
for f in fns:
    try:
        raise f()
    except ValueError as e:
        print('Caught:', e.args[0])
print('Final err:', err if 'err' in locals() else 'undefined')
