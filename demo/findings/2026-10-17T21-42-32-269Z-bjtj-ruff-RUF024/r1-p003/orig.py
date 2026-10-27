keys = iter(['a','b'])
d = dict.fromkeys(keys, [])
print('keys before:', list(keys))
try:
    second = dict.fromkeys(keys, [])
except Exception as e:
    print(type(e).__name__, str(e))
