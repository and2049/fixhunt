str = 'overridden'  # shadow built-in
mapping = {'a': 'value', 'str': 'also_used'}  # str used in format
fmt = '%(a)s %(str)s'
result = fmt % mapping
print('Result:', result)
# Later, str is reused as built-in via recovery
try:
    s = str([1, 2, 3])
except Exception as e:
    print('str recovery failed:', type(e).__name__, str(e))
else:
    print('str recovery:', s)
