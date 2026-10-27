d = {'a': 1, 'b': 2}
for k, v in d.items():
    gen = (x for x in [v] if x > 0)  # gen uses v
    print(list(gen))
