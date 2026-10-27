# This hazard concerns module-level behavior; the rule does not fire here.
# We include a split but it's not indexed, so expect_trigger=False.
s = 'hello world'
print(s.split())  # no indexing -> rule silent
