try:
    if 'missing' in d:
        del d['missing']
except KeyError as e:
    print('Caught:', type(e).__name__, str(e))
d = {}
# This block does not trigger the rule because it's inside try-except
# but we include it to show context; no trigger expected
