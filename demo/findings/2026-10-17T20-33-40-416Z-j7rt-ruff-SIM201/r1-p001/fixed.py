class C:
    def __init__(self):
        self.count = 0
    def __eq__(self, other):
        self.count += 1
        return True
c = C()
total = 0
for _ in range(2):
    if not c == c:   # Triggers SIM201
        total += 1
print(f'eq_calls={c.count}, result={total}')
