state = []
def log(n):
    state.append(f'called {n}')
    return n * 2
print('Start:', state)
try:
    val = bin(log(3)).count('1')
except Exception as e:
    print(f'Error: {type(e).__name__}: {e}')
print('After bin(log(3)).count(\'1\'):', state)
state.clear()
state.append('reset')
try:
    val = bin(log(5)).bit_count()
except Exception as e:
    print(f'Error: {type(e).__name__}: {e}')
print('After bin(log(5)).bit_count():', state)
