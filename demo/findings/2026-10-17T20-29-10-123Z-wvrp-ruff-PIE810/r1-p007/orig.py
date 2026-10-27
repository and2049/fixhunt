s = b'hello'
try:
    if s.startswith(b'h') or s.startswith(b'he'):
        print('match')
except Exception as e:
    print(type(e).__name__, e)
