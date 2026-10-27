side_effect_log = []
def side_effect_func():
    side_effect_log.append('called')
    return type

class SideEffectTest:
    __metaclass__ = side_effect_func()  # This should trigger side effect
    y = 2
    # After fix, the line is removed, so side effect should not happen on class definition
    # But we already called it during class creation
    print('Side effect log:', side_effect_log)
    print('Log length:', len(side_effect_log))
