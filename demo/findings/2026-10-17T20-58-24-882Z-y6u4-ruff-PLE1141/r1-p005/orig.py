i = 0
side_effects = []

def get_dict():
    side_effects.append(f'dict_call_{i}')
    global i
    i += 1
    return {'a': 1}

# Rule triggers on: for k, v in get_dict():
# But wait — rule only fires on simple dict variables, not calls!
# So we need a variable that is assigned from a call with side effect
# Let's do:
d = get_dict()  # side effect happens here
print('side_effects after assignment:', side_effects)
result = []
for k, v in d:  # <- TRIGGER: d is already evaluated
    result.append((k, v))
    side_effects.append(f'in_loop_{len(result)}')
print('result:', result)
print('side_effects final:', side_effects)
# Fix would do: for k, v in d.items(): same d, so no difference in eval timing
# But to show hazard: suppose we had a property that returns dict and has side effect
class Obj:
    @property
    def d(self):
        side_effects.append('prop_call')
        return {'x': 99}

o = Obj()
side_effects.clear()
i = 0
# Now: for k, v in o.d:  # <- but rule doesn't fire on attribute! skip for now
# We'll save attribute hazard for #6
print('skipping — not attribute')
