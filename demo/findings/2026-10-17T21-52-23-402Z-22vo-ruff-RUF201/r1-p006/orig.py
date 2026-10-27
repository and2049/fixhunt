import tomllib
with open('config.toml', 'w') as f:
    f.write('[tool.ruff]\nselect = ["F401", "E302"]\n')
toml = tomllib.load(open('config.toml', 'rb'))
names = toml['tool']['ruff']['select']
print(' & '.join(sorted(names)))
