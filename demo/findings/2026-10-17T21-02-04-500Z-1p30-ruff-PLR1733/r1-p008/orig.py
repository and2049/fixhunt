import os
os.mkdir('tmpdir')
os.symlink('tmpdir', 'link_to_tmpdir')
d = {'link': 'link_to_tmpdir'}
trace = []
for k, v in d.items():
    trace.append('start')
    p = os.path.realpath(d[k])  # triggers PLR1733: follows symlink via d[k]; fix would use v (string)
    trace.append(p)
    try:
        os.stat(d[k])           # also triggers PLR1733 in same loop
    except FileNotFoundError as e:
        trace.append(('stat error', e))
print('trace:', trace)
os.unlink('link_to_tmpdir')
os.rmdir('tmpdir')
