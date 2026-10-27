def side_effect():
    print("side effect")
    return IOError

try:
    raise side_effect()("delayed")  # RULE REWRITES the returned IOError -> OSError; side effect must happen
except OSError as e:
    print(f"Caught after side effect: {type(e).__name__}")
