TOML_SELECT = ['F401']  # unused-import
TOML_EXTEND_SELECT = ['W291']  # trailing-whitespace
# Assume we map back for logging
def to_code(name):
    rev = {'unused-import': 'F401', 'trailing-whitespace': 'W291'}
    return rev.get(name, name)
codes = [to_code(n) for n in TOML_SELECT + TOML_EXTEND_SELECT]
print('Mapped codes:', ','.join(codes))
# Simulate future Ruff renaming F401 -> something-else
# Today’s fix would be wrong if mapping changes
