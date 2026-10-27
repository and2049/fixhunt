try:
    x = '%s' % [1, 2]
except (TypeError, ValueError):
    print('caught:', type(e).__name__)
