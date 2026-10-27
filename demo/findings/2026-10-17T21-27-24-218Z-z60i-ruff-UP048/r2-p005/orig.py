True = 1  # shadow built-in True
while 1:
    print(True, type(True))  # Should be 1, int
    break
# Restore? Not needed; show effect
print('After loop, True =', True, type(True))
del True  # restore built-in if possible
try:
    print(True)
except Exception as e:
    print(type(e).__name__, e)
