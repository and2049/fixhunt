counter = 0

def get_binary_string():
    global counter
    counter += 1
    return f'0b{counter:04b}'  # Returns '0b0001', '0b0002', etc.

# First call
s1 = get_binary_string()
print('After s1, counter:', counter)
try:
    # Rule fires: int(s1[2:], 2)
    val1 = int(s1[2:], 2)
    print('Val1:', val1, 'Counter after int:', counter)
except Exception as e:
    print('Error1:', type(e).__name__, str(e))

# Second call - should be different if side effects duplicated
s2 = get_binary_string()
print('After s2, counter:', counter)
try:
    # If fix were applied: int(s2, 0) - but only one call to get_binary_string for s2
    val2 = int(s2, 0)
    print('Val2:', val2, 'Counter after int:', counter)
except Exception as e:
    print('Error2:', type(e).__name__, str(e))
print('Final counter:', counter)
