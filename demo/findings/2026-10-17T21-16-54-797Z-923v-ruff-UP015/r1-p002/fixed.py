# This hazard only manifests under Python 2.
# We simulate the divergence by showing what Python 2 would do.
try:
    u = b'\xc3\xa9'.decode('utf-8')  # é
    with open('tmp.txt', 'wb') as f:
        f.write(u.encode('utf-8'))
    with open('tmp.txt') as f:  # trigger in Py2, but we suppress fire
        data = f.read()
    print('Read:', repr(data))
except Exception as e:
    print(type(e).__name__, e)
import os; os.remove('tmp.txt') if 'tmp.txt' in locals() else None
