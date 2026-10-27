from typing import get_type_hints
import tomllib
with open('ruff.toml', 'w') as f:
    f.write('[tool.ruff]\nselect = ["F841"]\n')
toml = tomllib.load(open('ruff.toml', 'rb'))
code = toml['tool']['ruff']['select'][0]
def func(x: code) -> None:  # type annotation uses code string
    pass
try:
    hints = get_type_hints(func)
    print(hints.get('x', 'missing'))
except Exception as e:
    print(f'{type(e).__name__}: {e}')
