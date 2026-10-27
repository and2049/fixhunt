x = [1, 2, 3]
# Rule fires here: rewrites {i for i in x} to set(x) inside lambda
func = lambda: {i for i in x}
print(f'Before rebinding: {func()}')
x = [4, 5, 6]  # Rebinding x
print(f'After rebinding:  {func()}')
# Now test with set(x) version - same behavior since set(x) also uses current x
# But to show hazard, we need case where timing differs - use mutable default
x = [1, 2, 3]
def make_func():
    return lambda: {i for i in x}  # Comprehension version
f1 = make_func()
x = [4, 5, 6]
print(f'Comprehension lambda after rebinding: {f1()}')
# Reset for set() test
x = [1, 2, 3]
def make_func_set():
    return lambda: set(x)  # What rule would produce
f2 = make_func_set()
x = [4, 5, 6]
print(f'set() lambda after rebinding:       {f2()}')
