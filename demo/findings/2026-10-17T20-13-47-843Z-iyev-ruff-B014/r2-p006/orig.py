import inspect

def func():
    try:
        raise ValueError
    except (ValueError, TypeError):  # not redundant, so rule should not fire
        pass

handler_tuple = None
for name, cell in inspect.getclosurevars(func).nonlocals.items():
    if isinstance(cell, tuple) and all(isinstance(t, type) for t in cell):
        handler_tuple = cell
        break

print('Handler tuple:', handler_tuple)
print('Length:', len(handler_tuple) if handler_tuple else 0)
print('Types:', [t.__name__ for t in handler_tuple] if handler_tuple else [])
