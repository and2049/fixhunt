class GenTest:
    gen = (x for x in range(2))
    gen = list(gen)
print(list(GenTest.gen))
