mutations = []
class MutableItem:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f'Item({self.value})'
    def mutate(self):
        self.value *= 10
        mutations.append(id(self))
items = [MutableItem(i) for i in range(3)]
# During list comprehension build, we could mutate items if we had access.
# But comp expression only sees each item.
# Instead: make comprehension expression mutate a global.
counter = [0]
def increment_and_return(x):
    counter[0] += 1
    return x * counter[0]
s1 = set([increment_and_return(i) for i in [1,2,3]])  # List comp: increment called 1,2,3 in order
print('Mutation log (list-based):', counter[0])
print('Result:', s1)
counter[0] = 0
s2 = {increment_and_return(i) for i in [1,2,3]}     # Set comp: same call order
print('Mutation log (set-literal):', counter[0])
print('Result:', s2)
# Same.
# Hazard: if list was built and then mutated before set() call.
# Example: lst = [expr for ...]; lst.append(...); s = set(lst)
# Rule doesn't fire on that.
# We need to make the list comp inside set() be the only reference, but imagine:
# Developer assumes they can insert a debugging mutation between list creation and set() call.
# After refactor, no intermediate list exists to mutate.
# Show: if we could mutate the list during its construction (impossible).
# Instead: use side effect in expression that depends on list length so far.
# But list comp doesn't expose partial list.
# We simulate by having expression read a global that tracks how many items processed.
processed_count = []
def process(x):
    processed_count.append(len(processed_count))  # Index of this item
    return x * 10
items = [1,2,3]
s1 = set([process(x) for x in items])  # processed_count: [0,1,2]
print('Processed indices (list-based):', processed_count)
print('Result:', s1)
processed_count.clear()
s2 = {process(x) for x in items}       # processed_count: [0,1,2]
print('Processed indices (set-literal):', processed_count)
print('Result:', s2)
# Same.
# Final attempt: hazard is that list() constructor is explicit about creating list; set literal hides it.
# For teaching, removing list() may obscure intent.
# We output trace showing same behavior but note that intermediate list is gone.
print('Note: intermediate list no longer exists for inspection')
