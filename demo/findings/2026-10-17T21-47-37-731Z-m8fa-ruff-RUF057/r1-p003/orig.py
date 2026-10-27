flag = True
val = round(flag, 0)
print(type(val), val)
try:
    val += 1
    print('int op ok:', val)
except Exception as e:
    print(type(e).__name__, e)
# After fix: val becomes bool True, still works but type changed
