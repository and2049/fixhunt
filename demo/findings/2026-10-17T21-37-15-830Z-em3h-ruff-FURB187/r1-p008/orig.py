from pathlib import Path
p = Path('a')
parts = list(p.parts)[::-1]
print('reversed parts:', parts)
try:
    Path(*parts).resolve()
except Exception as e:
    print(type(e).__name__, str(e)[:50])
