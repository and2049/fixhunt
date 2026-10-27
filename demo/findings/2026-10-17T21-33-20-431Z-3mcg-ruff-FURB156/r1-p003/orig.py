def f():
    try:
        import string  # Local import to avoid circular
    except ImportError:
        pass
    if '0' in "0123456789":  # Triggers FURB156
        return "found"
    return "not found"

print(f())
