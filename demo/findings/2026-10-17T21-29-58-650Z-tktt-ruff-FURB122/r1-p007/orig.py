f = open('tmp.bin', 'wb')
try:
    for x in ['a', 'b']:
        f.write(x.encode())  # correct: bytes
    f.close()
    f = open('tmp.bin', 'wb')
    for x in ['a', 'b']:
        f.write(x)  # error: str in binary mode
except Exception as e:
    print('expected error:', type(e).__name__, str(e))
finally:
    if not f.closed:
        f.close()
