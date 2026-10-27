from typing import cast, List
def main():
    y = cast(T, x)  # Should be cast(str, x)
    T = list  # Now T is the lambda
    try:
        print('z:', z)
    except Exception as e:
        print('Error after redefinition:', type(e).__name__, str(e))
if __name__ == '__main__':
    main()
