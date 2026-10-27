def get_key():
    return 'dynamic'
# Ignored variable used in dict construction
tmp = get_key()  # ruff: ignore[F841]
d = {tmp: 'value', 'static': 1}
print(d.get('dynamic', 'missing'))
