import sys
mod = sys.modules[__name__]
mod.shared_state = 0

def update_state():
    mod.shared_state += 1
    return mod.shared_state

class FakeDict:
    def keys(self):
        update_state()
        return {'x': 1}.keys()

fd = FakeDict()
if 'x' in fd.keys():
    pass
print(f'Shared state: {mod.shared_state}')
