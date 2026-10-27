state = []
class DictLike:
    def keys(self):
        state.append('keys')
        return {'x': 1}.keys()
    def values(self):
        state.append('values')
        return {'x': 1}.values()
    def items(self):
        state.append('items')
        return {'x': 1}.items()

d = DictLike()
print('State before:', state)
_ = list(zip(d.keys(), d.values()))  # keys() then values()
print('State after zip:', state)
state.clear()
_ = list(d.items())  # items() call
print('State after items:', state)
