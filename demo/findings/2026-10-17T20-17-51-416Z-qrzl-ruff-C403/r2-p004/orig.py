construction_order = []
class Logger:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'<{self.name}>'
    def __hash__(self):
        return hash(self.name)
    def __eq__(self, other):
        return isinstance(other, Logger) and self.name == other.name
items = [Logger('a'), Logger('b'), Logger('c')]
# Build set via list comp: order of evaluation is items order, but set discards duplicates.
# No duplicates here, so set() will have arbitrary order, but list comp ran in order.
s1 = set([str(obj.name) for obj in items])  # List comp: logs in items order via str()? No, str doesn't log.
# Make __str__ log construction order.
def log_name(obj):
    construction_order.append(obj.name)
    return obj.name
s1 = set([log_name(obj) for obj in items])  # Logs a,b,c in order
print('Construction order (list-based):', construction_order)
construction_order.clear()
s2 = {log_name(obj) for obj in items}     # Logs a,b,c in order (same)
print('Construction order (set-literal):', construction_order)
# To see hazard: if code later iterated set expecting list order.
# But set order is arbitrary; logging during construction same.
# Hazard: developer thought set() preserved list order for debugging, but refactor makes it look intentional.
# Add duplicate to force non-trivial set building.
items = [Logger('a'), Logger('b'), Logger('a'), Logger('c')]
construction_order.clear()
s1 = set([log_name(obj) for obj in items])  # Logs a,b,a,c
print('With dup - construction order (list-based):', construction_order)
print('Result:', s1)
construction_order.clear()
s2 = {log_name(obj) for obj in items}     # Logs a,b,a,c
print('With dup - construction order (set-literal):', construction_order)
print('Result:', s2)
# Same logs. No behavioral change.
# Instead: make hazard about relying on list() intermediate for inspection.
# Example: debug prints list before set conversion.
items = [1,2,3]
temp = [x*2 for x in items]  # Not rewritten
print('Intermediate list (for debugging):', temp)
s = set(temp)                 # Not a comprehension inside set()
print('Final set:', s)
# Rule doesn't fire here.
# Make it fire: set([x*2 for x in items])
construction_order.clear()
def record(x):
    construction_order.append(x)
    return x*2
items = [1,2,3]
s1 = set([record(x) for x in items])  # Logs 1,2,3
print('Intermediate values recorded (list-based):', construction_order)
construction_order.clear()
s2 = {record(x) for x in items}       # Logs 1,2,3
print('Intermediate values recorded (set-literal):', construction_order)
# Still same.
# Conclusion: no semantic hazard, but we output as required.
