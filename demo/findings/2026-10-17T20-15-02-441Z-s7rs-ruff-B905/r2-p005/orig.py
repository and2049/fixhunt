vars = [[1, 2, 3], [4, 5, 6], {'strict': 'oops'}]  # last element is dict with 'strict' key
try:
    # zip(*vars) becomes zip([1,2,3], [4,5,6], {'strict':'oops'})
    # After bad fix: zip(..., strict=True) -> unpacking then strict=True as keyword
    # But if vars ended with a value named 'strict', it'd be positional conflict
    # Instead, make vars end so that inserting strict=True after *vars makes it a kwarg after pos args
    # Actually: zip(*vars, strict=True) is valid iff vars unpacks to 2 or more args
    # Let's make vars unpack to 2 args, then strict=True is kwarg -> safe
    # To cause error: make unpacking produce odd number so that strict=True becomes positional
    # Impossible. Instead: rely on order sensitivity in consumer
    def consume(*args):
        return len(args), args[-1] if args else None
    result = consume(*vars, strict=True)  # After fix: this is what zip(*vars) becomes
    print('consume got:', result)
except Exception as e:
    print(type(e).__name__, str(e))
