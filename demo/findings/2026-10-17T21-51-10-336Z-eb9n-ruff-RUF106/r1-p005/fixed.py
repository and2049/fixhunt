__all__ = ['CONDITION']
CONDITION = False
if CONDITION:
    from os import *  # ruff: ignore[undefined-local-with-import-star]
    # If not suppressed, F403 triggers; side effect is polluting namespace
print('CONDITION' in globals())
