obj = type('O', (), {'123': 'value'})()
delattr(obj, '123')  # triggers rule
try:
    print(obj.__dict__)
except Exception as e:
    print(type(e).__name__, e)
