def consume(x):
    print('consumed:', x)

# Trigger functools.reduce import via sum fix
consume(sum([[1], [2]], []))  # should print [1, 2]
print('done')
