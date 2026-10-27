cond = [True]
def get_cond():
    val = cond[0]
    cond.clear()
    cond.append(False)
    return val
branch_taken = None
x = 1 if get_cond() else 2
# Simulate what not(not(x)) does internally
first_eval = branch_taken := (1 if get_cond() else 2)
second_eval = branch_taken := (1 if get_cond() else 2)
print(f'First branch eval: {first_eval}, Second branch eval: {second_eval}')
# Actual code under test
try:
    result = not (not (1 if get_cond() else 2))
except Exception as e:
    print(f'Error: {e}')
else:
    print(f'Result: {result}')
