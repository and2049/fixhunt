import tomllib
with open('ruff.toml', 'w') as f:
    f.write('[tool.ruff]\nselect = ["F401", "unused-import"]\n')
toml = tomllib.load(open('ruff.toml', 'rb'))
select = toml['tool']['ruff']['select']
print(len(select))
print('dup' if len(select) != len(set(select)) else 'unique')
