import tomllib, json
with open('.ruff.toml', 'w') as f:
    f.write('[tool.ruff]\nignore = ["W291"]\n')
data = tomllib.load(open('.ruff.toml', 'rb'))
codes = data['tool']['ruff']['ignore']
if all(c.isdigit() for c in ''.join(codes)):
    print('legacy_ok')
else:
    print('legacy_broken')
