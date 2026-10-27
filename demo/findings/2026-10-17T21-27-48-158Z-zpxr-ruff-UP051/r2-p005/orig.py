import abc

decorator_log = []

def logged_abstractclassmethod(func):
    decorator_log.append('wrap_acm')
    return abc.abstractclassmethod(func)

# Build class dynamically
attrs = {
    '__module__': '__main__',
    'dynamic_method': logged_abstractclassmethod(lambda cls: 'dynamic')
}

DynamicCls = type('DynamicCls', (abc.ABC,), attrs)

# Now simulate what autofix would do: replace with @classmethod + @abstractmethod
# But order matters: if abstractmethod goes first, it breaks
try:
    obj = DynamicCls()
    result = obj.dynamic_method()
    decorator_log.append(f'result:{result}')
except Exception as e:
    decorator_log.append(f'{type(e).__name__}:{e}')

print('|'.join(decorator_log))
