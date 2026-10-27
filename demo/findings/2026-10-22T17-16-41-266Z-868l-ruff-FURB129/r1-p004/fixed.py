with open('tmp.txt', 'w') as f:
    f.write('0\n1\n')

with open('tmp.txt') as fp:
    trace = []
    for line in fp:  # Rule triggers here
        trace.append(str(bool(fp)))  # bool(fp) is True for open file
        if len(trace) >= 2:
            break
print(','.join(trace))
