__all__ = ['value']
value = str('hello')  # This is the exported value
def get_value():
    return value
print(get_value())
