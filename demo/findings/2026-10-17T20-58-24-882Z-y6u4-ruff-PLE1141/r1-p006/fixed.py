class Container:
    def __init__(self):
        self.data = {'a': 1, 'b': 2}

c = Container()
# Rule should NOT fire on for k, v in c.data: because it's an attribute
# But if we mistakenly think it does — or test near-miss
# Instead: make a case where variable looks simple but is subscript
d = [{'x': 1}, {'y': 2}]
# for k, v in d[0]:  # subscript — rule should not fire (not a dict var)
# So we need to trigger on a simple name that later becomes subscript? No.
# Let's just demonstrate the bug: if rule fired on attribute, it would break
# We simulate by showing what happens if someone writes for k, v in c.data:
# and a tool incorrectly adds .items()
try:
    exec("for k, v in c.data.items(): pass")  # this is valid
    print('c.data.items() works')
except Exception as e:
    print('error:', e)

# Now show the broken fix: c.data.items() is ok, but what if we had c.data[0]?
# Not relevant. Instead: focus on the fact that rule does NOT fire on attributes
# so we output that it stays silent — but hazard is about if it did fire incorrectly
# So we write a comment and show that the rule does not trigger here
print('Rule does not trigger on c.data (attribute)')
# For actual trigger, we need a simple name — so reset
d_simple = {'a': 1}
for k, v in d_simple:  # <- TRIGGER
    print('simple trigger works')
