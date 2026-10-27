from typing import TypeVar, TypeAliasType
T_co = TypeVar('T_co', covariant=True)
F = TypeAliasType('F', list[T_co])
def use(f):
    return isinstance(f([1]), F)
print(use(lambda x: x))
# After fix: `type F = list[T_co]` infers invariance, breaking covariance check
