import abc

registry = []

@staticmethod
@abc.abstractmethod
def register(item, storage=[]):
    storage.append(item)
    registry.append(tuple(storage))  # snapshot
    return storage

# After rewrite: @staticmethod\n@abc.abstractmethod
class Storage(abc.ABC):
    pass
Storage.register = register

try:
    s = Storage()
    s.register('a')  # storage=['a']
    s.register('b')  # storage=['a','b'] due to mutable default
    s.register('c')  # storage=['a','b','c']
    print(f'registry:{len(registry)} last:{registry[-1] if registry else []}')
except Exception as e:
    print(f'{type(e).__name__}:{e}')
