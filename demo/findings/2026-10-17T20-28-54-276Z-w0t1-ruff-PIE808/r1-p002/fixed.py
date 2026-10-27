r = range(3)
gen = (x*2 for x in r)
print(sum(gen))
print(sum(gen))  # exhausted
