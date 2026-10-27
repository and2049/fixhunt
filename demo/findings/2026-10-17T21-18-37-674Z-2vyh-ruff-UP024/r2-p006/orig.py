def gen():
    for i in range(3):
        if i == 1:
            raise IOError('at 1')
        yield i
g = gen()
try:
    for x in g:
        print('yielded:', x)
except IOError as e:
    print('gen IOError:', e)
except OSError as e:
    print('gen OSError:', e)
