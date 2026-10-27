super = 1
if super == 1:
    super = lambda: None  # rebind
try:
    super.__name__()  # triggers PLW0245 -> super().__name__()
except AttributeError as e:
    print(f'AttributeError: {e}')
