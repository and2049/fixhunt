import sys

# Track if hazardous module is imported
import_side_effects = []

# Simulate importing a module with side effects
if 'effect_mod' not in sys.modules:
    mod = type('effect_mod', (), {})
    mod._import_log = []
    def init_side():
        mod._import_log.append('initialized')
        return 42
    mod.CONSTANT = init_side()
    sys.modules['effect_mod'] = mod

effect_mod = sys.modules['effect_mod']

def get_lists():
    # Trigger import of effect_mod when called
    _ = effect_mod.CONSTANT  # access to trigger if not already
    return [[1], [2]]

print('Before call:', effect_mod._import_log)
try:
    # This sum call will trigger the fix -> add imports -> but we simulate
    # that the fix would insert imports HERE, which could cause side effects
    result = sum(get_lists(), [])
    print('After sum:', effect_mod._import_log)
    print('Result:', result)
except Exception as e:
    print('Error:', type(e).__name__, e)
