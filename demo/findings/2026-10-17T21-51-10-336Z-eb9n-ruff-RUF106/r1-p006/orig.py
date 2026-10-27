def process():
    """Process data if flag is set."""
    flag = True  # ruff: ignore[F841]
    if flag:
        return 'ok'
    return 'fail'
print(process())
