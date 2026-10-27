import abc
log = []
def make_dec(name):
    log.append(f'dec_{name}')
    def dec(f):
        log.append(f'apply_{name}')
        return f
    return dec

@make_dec('outer')
@property
@abc.abstractmethod
@make_dec('inner')
def prop(self):
    log.append('prop_body')
    return 42

class C(abc.ABC):
    pass
C.prop = prop

try:
    c = C()
    _ = c.prop  # triggers descriptor
    log.append('accessed')
except Exception as e:
    log.append(f'{type(e).__name__}:{e}')

print('|'.join(log))
