from typing import cast, List
def main():
    x = [1, 2, 3]
    # Keyword form: should trigger rule on typ=
    y = cast(typ=List[int], val=x)
    print('Length via keyword:', len(y))
    # After fix: autofix might not recognize keyword args and do nothing
    # Or worse, quote the first positional arg (which doesn't exist)
    # Simulate bad fix: if it tried to quote 'typ' or messed up keywords
    try:
        # This is safe: keyword args are preserved
        z = cast(typ=List[int], val=[4, 5])
        print('Second call:', z)
    except Exception as e:
        print('Error in keyword cast:', type(e).__name__, str(e))
    # To show dependency: if we change List[int] to a var, and fix breaks
    T = List[int]
    # Rule should fire on typ=T
    w = cast(typ=T, val=x)
    print('Via var:', len(w))
if __name__ == '__main__':
    main()
