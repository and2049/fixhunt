chunks = [b'ab', b'cd']
result = sum(chunks, b'')  # bytes concatenation
print('bytes result:', result)
try:
    sum([[1, 2]], '')  # mixing list and str start - should fail
except TypeError as e:
    print('error:', type(e).__name__, str(e))
