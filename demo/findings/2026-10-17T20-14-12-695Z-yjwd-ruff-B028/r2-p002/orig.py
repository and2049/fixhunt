import warnings

counter = [0]
def msg():
    counter[0] += 1
    return f'message-{counter[0]}'

warnings.warn(msg(), category=UserWarning)
print('counter:', counter[0])
