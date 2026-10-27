import abc
ac = abc.abstractclassmethod  # alias

# This line should NOT trigger UP051 because ac is not abc.abstractclassmethod
@ac
def cls_method(cls):
    return 'cls_result'

# Verify it works as abstractclassmethod
class Base(abc.ABC):
    pass

try:
    Base.cls_method = cls_method
    b = Base()
    result = b.cls_method()
    print(f'success:{result}')
except Exception as e:
    print(f'{type(e).__name__}:{e}')
