print('--- Hazard 8: File modes and truncation ---')
# We show that if the round call is used to determine a file mode or size, and removing it changes the type or value,
# it affects file operations.
# Example: open(file, 'w') vs open(file, str(round(5,0))) — but modes are strings.
# round(5,0)=5 -> str(5)='5' -> invalid mode.
# Not helpful.
# Example: truncating a file to a size.
# With open('test.txt', 'w+') as f:
#     f.write('hello')
#     f.truncate(round(5, 0))  # truncate to 5 bytes
# After fix: f.truncate(5) -> same.
# But if round(5,0) returns int 5, same.
# We need: the truncate size is expected to be float, but truncate requires integer.
# No.
# We use: writing non-str data to write() — but write requires str or bytes.
# Example: f.write(round(5, 0)) -> TypeError: write() argument must be str, not int
# After fix: f.write(5) -> same error.
# No difference.
# But if we do: f.write(str(round(5, 0))) -> writes '5'
# After fix: f.write(str(5)) -> same.
# We need: the write call is expecting a boolean for some reason — no.
# We use: the round call is used to compute a number that is then converted to bytes via int.to_bytes,
# and if the type is bool, it fails.
# Example:
# n = round(True, 0)  # 1 (int)
# b = n.to_bytes(1, 'big')  # b'\x01'
# After fix: n = True -> True.to_bytes(1, 'big') -> AttributeError: 'bool' object has no attribute 'to_bytes'
# Because bool does not inherit to_bytes from int in a way that it’s accessible?
# Let’s check: in Python, bool is a subclass of int, so True.to_bytes(...) should work.
# Test: >>> True.to_bytes(1, 'big')
# b'\x01'
# It works!
# So no error.
# We use: the code uses the value in a context where it is passed to a C extension that expects exact int type.
# But we can’t.
# We use: the value is used in a struct.pack format — which requires integer.
# struct.pack('b', True) works.
# We use: the value is used as a length in bytes() constructor.
# bytes(5) -> b'\x00\x00\x00\x00\x00'
# bytes(True) -> b'\x00'  # because bool(True) is 1
# Different!
# bytes(n) creates a bytes object of length n initialized with null bytes.
# bytes(5) -> 5 zero bytes
# bytes(True) -> bytes(1) -> 1 zero byte
# Different length!
# And round(True,0) is a firing shape.
# Perfect.
# We’ll use that.
import os

filename = 'test_output.bin'
if os.path.exists(filename):
    os.remove(filename)

# Write bytes based on round(True, 0)
n = round(True, 0)  # Should be 1 (int) -> bytes(n) = b'\x00'
# After fix: n = True -> bytes(True) = b'\x00' -> same?
# Wait: bytes(1) = b'\x00'
# bytes(True) = bytes(1) = b'\x00' -> same.
# Because bool(True) is 1.
# So bytes(n) depends on int(n), and int(True)==1, int(1)==1.
# Same.
# We need: bytes(n) where n is used as the literal value to repeat — no, bytes(n) makes n copies of b'\x00'.
# We want: to create a bytes object containing the integer value as a single byte.
# Then we should use: bytes([n])
# bytes([5]) -> b'\x05'
# bytes([True]) -> b'\x01'  # because True is 1
# Different!
# And round(True,0) -> [1] -> b'\x01'
# After fix: [True] -> b'\x01' -> same?
# [1] and [True] are different lists, but when passed to bytes(), both become b'\x01' because bytes() converts each element to int.
# bytes([1]) -> b'\x01'
# bytes([True]) -> b'\x01'
# Same.
# We use: bytearray(n) -> same as bytes(n).
# We use: the value is used to initialize an array of a specific type where the type checker is strict.
# No.
# We use: the value is used in a numpy array — but we can’t use numpy.
# We use: the value is used as the argument to chr().
# chr(65) -> 'A'
# chr(True) -> chr(1) -> '\x01' -> different!
# And round(True,0) -> 1 -> chr(1) -> '\x01'
# After fix: True -> chr(True) -> chr(1) -> '\x01' -> same!
# Because chr converts to int.
# Same.
# We use: the value is used in a format specifier that expects int but we rely on it being non-boolean for width.
# No.
# We use: the value is used to create a set where we expect the element to be int, but bool is considered equal.
# Still.
# We give up and use: the file is opened in a mode that is constructed from the round result, and we show that the mode string differs.
# Example:
# mode = str(round(5, 0))  # '5'
# After fix: str(5) -> '5' -> same.
# But if we do: mode = 'w' + str(round(5, 0))  # 'w5'
# After fix: 'w5' -> same.
# Not helpful.
# We use: the round call is used to determine the buffer size in a read, and we show that the number of bytes read differs.
# But read(size) — size must be integer.
# If round(5,0)=5, same.
# We use: the expression is round(5.5, 0) — but rule does NOT fire.
# We violate and use a non-integer-typed expr that we trick the rule into firing? Not allowed.
# We use: the expression is 5.0 — but rule does not fire.
# We must use a firing shape.
# We use: round(5, 0) -> 5.
# And we show that if the code had written round(5.0, 0) (which it didn’t), it would be different.
# Not honest.
# We use: the code reads the file and interprets the bytes as an integer, and we show that the value written differs because of type.
# But we write the same value.
# Final idea: we write the result of round() to a file as text, and we show that the written text differs because one writes '1' and the other writes 'True'.
# Example:
# with open('out.txt', 'w') as f:
#     f.write(str(round(True, 0)))
# After fix: f.write(str(True))
# str(round(True,0)) = str(1) = '1'
# str(True) = 'True'
# Different!
# And round(True,0) is a firing shape.
# Perfect.
# We’ll do that.
print('Writing to file...')
with open('output.txt', 'w') as f:
    f.write(str(round(True, 0)))

with open('output.txt', 'r') as f:
    content = f.read()
print('File content:', repr(content))
# Before fix: '1'
# After fix: 'True'
# Clean up
try:
    os.remove('output.txt')
except:
    pass
