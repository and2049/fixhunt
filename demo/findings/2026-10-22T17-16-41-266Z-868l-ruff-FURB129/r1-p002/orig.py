lines = ['a\n', 'b\n', 'c\n']
with open('tmp.txt', 'w') as f:
    f.writelines(lines)

with open('tmp.txt') as fp:
    trace = []
    while (line := fp.readline()) and len(trace) < 2:
        trace.append(line.strip())
    # Reset and trigger rule
    fp.seek(0)
    for x in fp.readlines():  # Rule triggers here
        trace.append(x.strip())
        if len(trace) >= 4:
            break
print('|'.join(trace))
