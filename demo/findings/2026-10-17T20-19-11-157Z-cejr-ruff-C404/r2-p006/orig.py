import sys
# Module-level dict comprehension that triggers rule
MAP = dict([(k, k) for k in ['a', 'b']])
# Simulate * import side effect by checking what's in globals after
if 'MAP' in globals():
    print('MAP defined as:', type(MAP).__name__)
    print('MAP contents:', MAP)
