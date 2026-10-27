def f():
    try:
        raise ValueError('x')  # This line must stay indented
        pass                   # Rule triggers: removable pass after stmt
    except ValueError as e:
        print('caught:', e)
    except Exception as e:
        print('unexpected:', e)
f()
