f = open('tmp.bin', 'wb')
try:
    f.writelines(x.encode() for x in ['a', 'b'])  # correct: bytes
    f.close()
    f = open('tmp.bin', 'wb')
    f.writelines(['a', 'b'])  # error: str in binary mode
except Exception as e:
    print('expected error:', type(e).__name__, str(e))
finally:
    if not f.closed:
        f.close()
