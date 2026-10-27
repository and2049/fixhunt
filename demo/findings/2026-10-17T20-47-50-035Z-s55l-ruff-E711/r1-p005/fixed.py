x = None
# Check if uninitialized before use
if x == None:  # safety guard for hot path
    x = 42
print(x)
