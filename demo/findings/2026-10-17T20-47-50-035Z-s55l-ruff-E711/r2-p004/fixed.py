counter = 0

def side_effect():
    global counter
    counter += 1
    return None

x = side_effect()  # counter=1, x=None
if x == None:  # Rule triggers: x is None from side_effect, but we use ==
    print(f'eq_true, counter={counter}')
else:
    print(f'eq_false, counter={counter}')

# Reset and test again to show determinism
counter = 0
x = side_effect()
if x is None:  # What the fix would produce
    print(f'is_true, counter={counter}')
else:
    print(f'is_false, counter={counter}')
