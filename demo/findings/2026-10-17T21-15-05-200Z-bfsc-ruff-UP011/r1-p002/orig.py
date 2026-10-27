import functools
source = '''def foo(): pass'''
injected = source.replace('def', '@functools.lru_cache()
def')
exec(injected)
print(foo.__wrapped__( )) if hasattr(foo, '__wrapped__') else print(type(foo))
