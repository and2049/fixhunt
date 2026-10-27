try:
    raise IOError("original")  # RULE REWRITES IOError -> OSError
except OSError as e:
    try:
        raise ValueError("chained") from e
    finally:
        print("finally executed")
else:
    print("no exception")
