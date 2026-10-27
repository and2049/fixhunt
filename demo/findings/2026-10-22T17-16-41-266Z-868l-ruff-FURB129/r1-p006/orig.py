def get_lines():
    with open('tmp.txt', 'w') as f:
        f.write('x\ny')
    with open('tmp.txt') as fp:
        # This annotation is evaluated at runtime in Python 3.7+
        lines: list[str] = list(fp.readlines())  # Rule does NOT trigger here (assignment)
        return [l.upper() for l in lines]

# Separate loop where rule DOES trigger
with open('tmp.txt') as fp:
    trace = []
    for line in fp.readlines():  # Rule triggers here
        trace.append(line.strip())
        if len(trace) >= 2:
            break
print(','.join(trace))
