from typing import TypeAlias
def get_type():
    print('Side effect')
    return 'int'
SideAlias: TypeAlias = f"{get_type()} | None"
print('Before use')
x: SideAlias = 5
print('After use')
