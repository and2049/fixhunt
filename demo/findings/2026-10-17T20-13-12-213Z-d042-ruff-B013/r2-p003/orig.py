try:
    b'\xff'.decode('utf-8')
except (UnicodeDecodeError,) as e:
    print(type(e).__name__, len(str(e)))
try:
    ''.encode('utf-8').decode('latin-1')
except (UnicodeEncodeError,) as e:
    print(type(e).__name__, len(str(e)))
