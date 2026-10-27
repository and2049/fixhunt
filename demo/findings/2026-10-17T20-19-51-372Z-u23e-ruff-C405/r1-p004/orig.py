trace = []
def make_list():
    trace.append('list made')
    return [1,1,2]
s = set(make_list())
print(''.join(trace), len(s))
