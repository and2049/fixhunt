from typing import TypeVar
T = TypeVar('T')
def append_to_list(x: T, lst=[]):
    lst.append(x)
    return lst
r1 = append_to_list(1)
r2 = append_to_list(2)
print(f"List 1: {r1}, List 2: {r2}, Same object: {r1 is r2}")
