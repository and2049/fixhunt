import tomllib
with open('temp.toml', 'w') as f:
    f.write('[tool.ruff]\nignore = [\n  "W291",\n  "E111"\n]\n')
toml = tomllib.load(open('temp.toml', 'rb'))
arr = toml['tool']['ruff']['ignore']
print(len(arr))
for item in arr:
    print(repr(item))
