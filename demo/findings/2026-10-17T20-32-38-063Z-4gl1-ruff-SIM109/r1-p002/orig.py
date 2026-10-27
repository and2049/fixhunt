x = []
y = []
z = [x, y]
if x == [] or y == []:
    z.append('matched')
print(f'z before: {z}')
# Simulate post-fix: if x in ((), ()):  # but we can't simulate fix directly
# Instead, show that the condition depends on two evals
# We'll show that mutating after first check affects second
x = [1]
y = []
if x == [] or y == []:
    print('inner')
else:
    print('outer')
print(f'x={x}, y={y}')
