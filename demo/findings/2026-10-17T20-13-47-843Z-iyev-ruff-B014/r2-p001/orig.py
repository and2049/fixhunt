# Test comment preservation
try:
    raise ValueError
except (Exception, # keep this comment
        ValueError):  # this should stay
    print('Caught:', type(__import__('sys').exc_info()[1]).__name__)
else:
    print('No exception')
finally:
    print('Finally ran')
