def process(*, ignore=('W291',), action='log'):  # W291 = trailing-whitespace
    print(f'Ignoring: {ignore[0]}')
    if action == 'log':
        return f'logged:{ignore[0]}'
    return ignore[0]
# Default captured at definition
out = process()
print(out)
# Later redefine? Can't, but show reliance
# If fix changes 'W291' to name, default still holds old string
# Unless function is redefined, but we don't — so behavior static
