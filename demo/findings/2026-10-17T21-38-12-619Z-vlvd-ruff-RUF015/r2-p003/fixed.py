prints = []
def make_seq():
    prints.append('start')
    for i in range(3):
        prints.append(f'yield {i}')
        yield i
    prints.append('end')
gen = make_seq()
# Result unused -> no iteration happens in rewrite
_ = list(gen)[0]  # Would trigger, but result used? No: we assign to _ then ignore
# Actually, we do use it: we assign to _, but then we don't use _ later.
# To avoid use, we must not assign or use the result.
# Let's not assign: just express it and discard.
list(make_seq())[0]  # This line: rule triggers, and we do NOT store result
print('prints so far:', prints)
# Now force consumption
list(make_seq())[0]  # Second trigger
print('prints after:', prints)
# Rule triggers twice: on both list(make_seq())[0]
