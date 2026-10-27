def get_a():
    print('A')
    return 'a'
def get_b():
    print('B')
    return 'b'
s = ' '
trace = []
trace.append(s.join((get_a(), get_b())))
trace.append(f'{get_a()} {get_b()}')
print('|'.join(trace))
