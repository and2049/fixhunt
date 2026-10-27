# Check if trailing comment survives rewrite
result = eval('1+1')  # noqa: PGH001  # this comment explains why we allow eval
print(result)
print('# this comment explains why we allow eval' in open(__file__).readlines()[1])
