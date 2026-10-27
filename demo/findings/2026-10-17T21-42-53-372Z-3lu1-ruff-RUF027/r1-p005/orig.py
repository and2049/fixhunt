vals = (i for i in [1,2])
s = ['Item {v}' for v in vals]
print('First use :', s)
print('Second use:', [x for x in s])
