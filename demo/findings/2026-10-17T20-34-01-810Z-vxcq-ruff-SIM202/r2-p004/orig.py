b1 = b'hello\n'
b2 = b'hello\n'
s1 = 'hello\n'
s2 = 'hello\n'
print('not b1 != b2:', not b1 != b2)
print('b1 == b2:', b1 == b2)
print('not s1 != s2:', not s1 != s2)
print('s1 == s2:', s1 == s2)
# After fix: not x != y -> x == y
print('Fixed b comparison:', b1 == b2)
print('Fixed s comparison:', s1 == s2)
# Same here, but show we checked
assert (not b1 != b2) == (b1 == b2)
assert (not s1 != s2) == (s1 == s2)
print('Byte/str comparisons consistent')
