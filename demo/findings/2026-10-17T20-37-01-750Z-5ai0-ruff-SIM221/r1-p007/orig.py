__all__ = ['flag']
flag = False

# Simulate star-import by direct use
print(flag or not flag)
flag = True
print(flag or not flag)
