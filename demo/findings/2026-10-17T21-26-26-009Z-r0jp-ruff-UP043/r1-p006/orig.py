from typing import Union, Generator
def process(x: Union[Generator[int, None, None], str]):
    if isinstance(x, str):
        return x.upper()
    return list(x)
print(process((i for i in [2])))
print(process('hello'))
