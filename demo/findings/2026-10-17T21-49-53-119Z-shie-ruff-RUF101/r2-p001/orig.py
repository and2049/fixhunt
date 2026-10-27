import sys
# Test: does rewrite touch 'PGH001' inside a string?
s = '\\'eval(cmd)\\'  # noqa: PGH001
print(repr(s))
if s == "'eval(cmd)'":
    print('PASS: string unchanged')
else:
    print('FAIL: string altered:', repr(s))
