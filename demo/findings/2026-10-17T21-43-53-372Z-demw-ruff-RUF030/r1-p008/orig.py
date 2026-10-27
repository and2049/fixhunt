import sys
output = []
def log(m, *, file=sys.stdout):
    file.write(m + '\n')
    return m
for dest in [sys.stdout, sys.stderr]:
    try:
        assert False, log('error', file=dest)
    except AssertionError as e:
        output.append(str(e))
    else:
        output.append('no raise')
print('|'.join(output))
