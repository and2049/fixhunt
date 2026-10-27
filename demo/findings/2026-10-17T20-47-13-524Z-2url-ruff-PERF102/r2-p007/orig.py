import sys
def trace(frame, event, arg):
    if event == 'line' and frame.f_locals.get('k') == 'a':
        if 'v' in frame.f_locals:
            print(f'v={frame.f_locals["v"]}')
        else:
            print("v missing")
    return trace
d = {'a': 1}
sys.settrace(trace)
for k, v in d.items():
    pass
sys.settrace(None)
