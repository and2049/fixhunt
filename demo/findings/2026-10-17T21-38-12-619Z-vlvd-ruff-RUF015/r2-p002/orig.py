def get_seq():
    raise ValueError('bad seq')
try:
    x = list(get_seq())[0]
except Exception as e:
    print('caught:', type(e).__name__, str(e))
    try:
        raise RuntimeError('handler failed') from e
    except Exception as e2:
        print('chained:', type(e2).__name__, str(e2))
        if e2.__cause__:
            print('cause:', type(e2.__cause__).__name__, str(e2.__cause__))
# Rule triggers on: list(get_seq())[0]
