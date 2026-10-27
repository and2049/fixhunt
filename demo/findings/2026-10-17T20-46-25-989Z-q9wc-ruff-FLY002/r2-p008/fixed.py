class BytesReturn:
    def __format__(self, spec):
        return b'bytes'
    def __str__(self):
        return 'str'
obj = BytesReturn()
try:
    j = '|'.join((obj,))
    print(f'Join result: {repr(j)}')  # -> 'str'
except Exception as e:
    print(f'Join error: {type(e).__name__}: {e}')
try:
    fs = f'{obj}|'  # -> b'bytes|' (bytes)
    print(f'F-string result: {repr(fs)}')
    # Downstream: if used where string expected
    print(fs.upper())  # AttributeError: bytes has no upper
except Exception as e:
    print(f'F-string downstream: {type(e).__name__}: {e}')
