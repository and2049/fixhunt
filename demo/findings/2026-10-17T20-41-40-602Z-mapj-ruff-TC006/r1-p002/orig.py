from typing import cast, List, Dict
# Type expression split across lines
MyType = Dict[
    str,
    List[int]
]
def main():
    data = {'a': [1, 2]}
    try:
        # This cast has a multiline first argument
        result = cast(
            MyType,
            data
        )
        print('Success:', result['a'])
    except Exception as e:
        print('Error during cast:', type(e).__name__, str(e))
    # After fix: the autofix might produce:
    # cast(
    #     "MyType,
    #     \n    str,
    #     \n    List[int]
    # ), data
    # which is invalid syntax due to broken string
    # We simulate by trying to eval the broken form
    try:
        broken = 'cast(\n    "MyType,\n    \nstr,\n    \nList[int]\n), data'
        # This would be a syntax error if parsed
        print('Broken form would fail to parse')
    except:
        pass
if __name__ == '__main__':
    main()
