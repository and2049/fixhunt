template = '%(name)s %d'
data = ({'name': 'Alice', 'extra': 99}, 42)
try:
    result = template % data
    print('Output:', result)
except Exception as e:
    print('Error:', type(e).__name__, str(e))
