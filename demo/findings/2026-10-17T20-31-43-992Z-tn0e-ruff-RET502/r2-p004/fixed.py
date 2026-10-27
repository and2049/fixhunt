__all__ = ['helper']

def helper():
    if config.get('skip'):
        return None
    return 'loaded'

config = {'skip': True}
print(helper())
config['skip'] = False
print(helper())
