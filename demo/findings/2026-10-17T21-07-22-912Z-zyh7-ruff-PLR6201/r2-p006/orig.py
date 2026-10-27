def gen():
    print('Generator called')
    yield 1
    yield 2
print(1 in (x for x in gen()))  # Rule does NOT fire: generator expression
# But if we had: 1 in [x for x in gen()] -> rule fires, eager eval
lst = [x for x in gen()]  # Rule fires here: list comprehension
print(1 in lst)  # Already printed 'Generator called' twice
