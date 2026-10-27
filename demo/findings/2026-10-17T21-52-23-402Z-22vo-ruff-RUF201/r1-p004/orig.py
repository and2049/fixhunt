import tomllib
with open('pyproject.toml', 'w') as f:
    f.write('[tool.ruff]\nselect = ["F401"]\nextend-select = ["F401"]\n')
toml = tomllib.load(open('pyproject.toml', 'rb'))
base = set(toml['tool']['ruff']['select'])
extra = set(toml['tool']['ruff']['extend-select'])
combined = list(base | extra)
print(sorted(combined))
