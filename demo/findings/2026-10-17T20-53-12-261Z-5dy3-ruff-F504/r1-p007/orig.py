# This comment is outside
mapping = {
    'keep': 'value',  # Important
    'remove': 42,   # TODO: remove this
}
result = 'Keep: %(keep)s' % mapping
print('Result:', result)
print('Mapping keys:', list(mapping.keys()))  # Should show both keys before fix
