def buggy(x):
    if x > 10:
        return x
    else:
        pass  # breakpoint here
result = buggy(5)
print("Result:", result)
# After fix, breakpoint is gone; no way to stop in else branch
