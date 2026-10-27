class A:
    shared = [1, 2]
    def __init__(self, val):
        self.instance_val = val
    @property
    def prop(self):
        print('prop accessed')
        return self.instance_val

a = A(99)
# Rule triggers on: not a.prop in a.shared
print('Before:')
try:
    result = a.prop not in a.shared
    print('not a.prop in a.shared:', result)
except Exception as e:
    print(type(e).__name__, str(e))
# Change shared after eval
a.shared.append(99)
print('After append:')
print('not a.prop in a.shared:', a.prop not in a.shared)
# Trigger again via lambda to show rewrite would not change behavior
f = lambda: a.prop not in a.shared
print('lambda:', f())
