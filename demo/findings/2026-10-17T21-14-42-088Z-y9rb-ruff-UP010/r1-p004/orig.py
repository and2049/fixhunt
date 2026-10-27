from __future__ import annotations

try:
    print('In try')
    raise ValueError('test')
except ValueError as e:
    print(f'Caught: {e}')
    raise RuntimeError('from value') from e
else:
    print('In else')
finally:
    print('In finally')
    # This line may be affected if import removal changes line numbers in traceback
    # but we check if the exception chain is preserved
    pass
