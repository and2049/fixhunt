counter = 0
def get_obj():
    global counter
    counter += 1
    return type('Obj', (), {'x': 42})()
obj = get_obj()
print(f'obj counter: {counter}')
val = get_obj().x  # get_obj called again -> counter=2
print(f'value: {val}, counter: {counter}')
# After fix: get_obj().x -> still calls get_obj() once, same behavior
# But if fix incorrectly cached object, would differ. Need a case where fix evaluates obj twice.
# Actually, B009 fix does not duplicate obj -- it's safe. So we must simulate a hazardous scenario where someone might think it's safe but isn't.
# Let's use a property with side effect on access.
