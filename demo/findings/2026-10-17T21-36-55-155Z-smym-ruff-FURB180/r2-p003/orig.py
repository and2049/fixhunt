class E(metaclass=abc.ABCMeta):
    shared = []
    def __init__(self, value=shared):
        self.value = value
        E.shared.append(1)
e1 = E()
e2 = E([99])
print(f'e1.value: {e1.value}, length: {len(e1.value)}')
print(f'e2.value: {e2.value}, length: {len(e2.value)}')
