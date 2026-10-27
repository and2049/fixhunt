import typing

T: typing.TypeAlias = int  # Rule triggers here

def __getattr__(name):
    if name == 'T':
        return 42  # Only called if T is not found normally
    raise AttributeError(name)

def __dir__():
    return ['T'] + [x for x in dir() if x != 'T']

print('Before any access:', end=' ')
try:
    print(T)
except AttributeError as e:
    print(f'AttributeError: {e}')

print('After defining T via getattr:', end=' ')
try:
    print(T)
except AttributeError as e:
    print(f'AttributeError: {e}')
