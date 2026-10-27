counter = 0
def get_mode():
    global counter
    counter += 1
    return 'r'
counter = 0
try:
    # Normal: open(file, get_mode()) -> get_mode called once
    with open('tmp.txt', get_mode()) as f:
        pass
    print('normal mode calls:', counter)
    counter = 0
    # After fix: if rule adds encoding as kwarg before **kwargs, but we don't have **kwargs.
    # Instead, simulate case where open is called via *args from tuple that includes mode.
    # Actually, better: the fix does not reorder unless **kwargs present.
    # So create a call with **kwargs to trigger reordering.
    def get_file():
        global counter
        counter += 1
        return 'tmp.txt'
    def get_mode():
        global counter
        counter += 1
        return 'r'
    counter = 0
    args = (get_file(), get_mode())
    kwargs = {}
    try:
        with open(*args, **kwargs) as f:  # Before fix: args[0], args[1]
            pass
        print('normal call order counters:', counter)
        counter = 0
        # After fix: becomes open(*args, encoding='utf-8', **kwargs)
        # Still same order: args[0], args[1], then kwarg
        # No change? Then hazard not met.
        # Need case where **kwargs exists and encoding inserted before it.
        # Let’s make kwargs non-empty.
        def get_kw():
            global counter
            counter += 1
            return {'buffering': -1}
        counter = 0
        args = (get_file(), 'r')
        kw_arg = get_kw()
        try:
            with open(*args, encoding='utf-8', **kw_arg) as f:  # Simulated fixed version
                pass
            print('fixed call order counters:', counter)
        except Exception as e:
            print('fixed error:', type(e).__name__, e)
    except Exception as e:
        print('error:', type(e).__name__, e)
finally:
    import os
    try: os.remove('tmp.txt')
    except: pass
