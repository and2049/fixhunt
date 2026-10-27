class MutableReturn:
    def __init__(self):
        self.state = 'original'
    def mutate(self):
        self.state = 'mutated'
        return self
class Obj:
    def __init__(self):
        self.call_count = 0
    def method(self):
        self.call_count += 1
        return MutableReturn().mutate() if self.call_count == 1 else MutableReturn()
obj = Obj()
try:
    # First call: returns mutated object
    # Second call: returns fresh object
    result = bool(obj.method())
    print(f'Method calls: {obj.call_count}, Result truthiness: {bool(result)}')
except Exception as e:
    print(f'Error: {e}')
