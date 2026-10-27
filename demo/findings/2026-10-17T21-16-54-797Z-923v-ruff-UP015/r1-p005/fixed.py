funs = []
for i in range(2):
    if (f := open(f'tmp{i}.txt')) is not None:  # trigger
        funs.append(lambda: f.read())
        f.close()
    else:
        funs.append(lambda: 'failed')
print([g() for g in funs])
import os; [os.remove(f'tmp{i}.txt') for i in range(2)]
