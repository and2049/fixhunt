a, b, c = 1, 2, 3
if a < b < c:
    pass  # Set breakpoint here to inspect a,b,c
print('Chain holds:', a < b and b < c)  # Same logic, but now expr stmt - no breakpoint hook
