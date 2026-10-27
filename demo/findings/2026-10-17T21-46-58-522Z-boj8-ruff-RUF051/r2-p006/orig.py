log = []
def risky_pop(d, k):
    log.append('pop-enter')
    if k == 'bad':
        raise ValueError('poison')
    return d.pop(k, None)
d = {'good': 1, 'bad': 2}
try:
    if 'good' in d:
        val = risky_pop(d, 'good')
        log.append(f'got {val}')
except ValueError as e:
    log.append(f'bad-value: {e}')
else:
    log.append('else: ok')
finally:
    log.append('finally')
print('|'.join(log))
