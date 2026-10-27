__all__ = ['CustomError']

class CustomError(Exception):
    pass

def func():
    try:
        raise CustomError('module side effect')
    except CustomError as e:
        print('Caught in func:', e)
        return len(__all__)

print(func())
