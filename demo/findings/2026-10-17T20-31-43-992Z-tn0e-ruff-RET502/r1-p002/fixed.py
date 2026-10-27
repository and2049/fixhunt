class CM:
    def __enter__(self): return self
    def __exit__(self, exc_type, exc, tb):
        if exc_type is ValueError:
            return None
        return False
with CM() as cm:
    raise ValueError('oops')
print(cm.__dict__.get('suppressed', 'no'))
