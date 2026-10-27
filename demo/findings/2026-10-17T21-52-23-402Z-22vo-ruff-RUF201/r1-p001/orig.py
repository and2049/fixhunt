import tomllib
with open('pyproject.toml', 'w') as f:
    f.write('[tool.ruff]\nselect = ["F401"  # check unused imports\n]\n')
toml = tomllib.load(open('pyproject.toml', 'rb'))
print(len(toml['tool']['ruff']['select']))
