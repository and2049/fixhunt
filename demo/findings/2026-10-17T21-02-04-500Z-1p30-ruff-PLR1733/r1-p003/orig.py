d = {'a': 1, 'b': 2}
trace = []
for k, v in d.items():
    trace.append(len(d))
    del d[k]  # triggers PLR1733: incorrectly would become del v (SyntaxError)
    trace.append(len(d))
try:
    for k, v in d.items():
        del d[k]
except Exception as e:
    trace.append(('error', type(e).__name__, str(e)))
print('trace:', trace)
