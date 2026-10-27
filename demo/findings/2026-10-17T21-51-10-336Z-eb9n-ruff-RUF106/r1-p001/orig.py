x = []
# Simulate conditional execution based on whether suppression works
for i in range(2):
    if i == 0:
        # Import that should trigger F401 if not suppressed
        import sys  # ruff: ignore[999]
        x.append('imported')
    else:
        x.append('rechecked')
print(len(x))
