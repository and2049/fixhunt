def f():
    super = lambda: None  # local shadows builtin
    try:
        super.__class__()  # triggers PLW0245 -> super().__class__()
    except AttributeError as e:
        print(f'AttributeError: {e}')
f()
