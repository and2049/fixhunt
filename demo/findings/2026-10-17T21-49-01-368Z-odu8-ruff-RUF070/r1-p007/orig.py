def gen():
    x = 42
    frame = None
    def capture_frame():
        nonlocal frame
        frame = frame  # This is a trick: we want to capture the frame at yield point
        # Instead, we inspect locals at first yield
        pass
    # We'll inspect locals by yielding a frame proxy
    yield x
    # Now yield locals() to see if 'x' is present
    # But we can't access frame directly -> alternative: use sys._getframe
    import sys
    yield sys._getframe().f_locals.copy()

# First value is 42, second is locals dict
g = gen()
first = next(g)
second = next(g)
print(f'First yielded: {first}')
print(f"'x' in locals: {'x' in second}")
print(f"Value of 'x' in locals: {second.get('x', 'MISSING')}")
