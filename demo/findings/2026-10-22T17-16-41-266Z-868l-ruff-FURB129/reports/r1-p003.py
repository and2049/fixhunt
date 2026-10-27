with open('tmp.txt', 'w') as f:
    f.write('apple\nbanana\ncherry')
with open('tmp.txt') as fp:
    trace = []
    for line in fp.readlines():  # Rule triggers here
        try:
            trace.append(f'{len(fp.readlines())}:{line.strip()}')
        except AttributeError as e:
            trace.append(f'ERR:{type(e).__name__}')
print(','.join(trace))
