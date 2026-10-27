REGISTERED = []
def register(name):
    REGISTERED.append(name)
register('mod')  # noqa: FAKE
from mod import *
print('mod' in REGISTERED)
