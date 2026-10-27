for i in range(2):
    if i == 0:
        pass  # should be skipped
    else:
        print('outer else', i)
# After fix, else binds to if, not for
