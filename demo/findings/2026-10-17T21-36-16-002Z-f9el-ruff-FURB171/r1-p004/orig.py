def f():
    x = b'\x00'
    # Rule triggers here: x in b'\x00'
    return x in b'\x00'
print(f())  # Should print True
# After fix: would be x == b'\x00'[0] -> b'\x00' == 0 -> False
# So output changes from True to False
