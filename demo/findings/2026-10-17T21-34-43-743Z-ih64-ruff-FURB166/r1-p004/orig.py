import array
arr = array.array('B', [48, 98, 49, 48, 49, 50])  # b'0b1010'
mv = memoryview(arr)
print('Original memoryview:', mv.tobytes())
try:
    sliced = mv[2:]  # memoryview of b'1010'
    # int() on memoryview? No, we need to convert to bytes first typically
    # But original code: int(mv[2:], 2) -> this will fail because memoryview not string/bytes
    result = int(mv[2:], 2)
    print('Slice result:', result)
except Exception as e:
    print('Original error:', type(e).__name__, str(e))
try:
    # What fix would produce: int(mv, 0) -> also fails, same error
    result2 = int(mv, 0)
    print('Fixed result:', result2)
except Exception as e:
    print('Fixed error:', type(e).__name__, str(e))
# To see difference, we need a case where mv[2:] works but mv doesn't with base 0
# But both fail similarly.
# Instead: suppose we have a function that expects to receive the slice for other use
def process(data):
    return data.tobytes()
slice_val = mv[2:]
processed = process(slice_val)
print('Slice processed:', processed)
# If rule fired, we'd lose the slice assignment above? No, the slice is still computed.
# Unless we inline: process(mv[2:]) becomes process(mv) after fix? No.
# Only the int() call changes.
# So make the int() call's result used in process
try:
    val = int(mv[2:], 2)
    processed_val = process(mv[2:])  # slice reused
    print('Val and processed:', val, processed_val)
except Exception as e:
    print('Error in reuse:', type(e).__name__, str(e))
