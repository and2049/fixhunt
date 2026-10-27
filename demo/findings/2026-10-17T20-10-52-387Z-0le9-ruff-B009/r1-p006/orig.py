counter = 0
side_effects = []

def get_obj():
    side_effects.append('get_obj called')
    counter_local = counter
    def inner():
        nonlocal counter
        counter += 1
        return type('Obj', (), {'attr': counter_local})()
    return inner()

x = getattr(get_obj(), 'attr')
print('x:', x, 'counter:', counter, 'side_effects:', side_effects)
