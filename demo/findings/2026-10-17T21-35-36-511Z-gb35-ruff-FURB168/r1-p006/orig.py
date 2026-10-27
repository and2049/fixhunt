def test():
    type = lambda: None  # shadow built-in
    x = None
    if isinstance(x, type(None)):  # uses local type -> type(None) -> None
        return 'local'
    return 'global'
print(test())
