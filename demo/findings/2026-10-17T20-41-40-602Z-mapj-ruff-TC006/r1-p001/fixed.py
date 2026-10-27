from typing import cast, List
T = List[int]
def main():
    x = [1, 2, 3]
    try:
        # This should work: T is a type
        y = cast('T', x)
        print('Before fix:', len(y))
    except Exception as e:
        print('Error before fix:', type(e).__name__, str(e))
    # After fix: cast('T', x) -> T becomes string literal, not a type
    # This will cause mypy/pyright to fail, but at runtime it's still a cast
    # However, if we later use y as a type (e.g. in isinstance), it breaks
    try:
        if isinstance(y, T):  # T is still List[int] here
            print('y is instance of T')
        else:
            print('y is not instance of T')
    except Exception as e:
        print('Error in isinstance:', type(e).__name__, str(e))
if __name__ == '__main__':
    main()
