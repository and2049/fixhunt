n = 5
f = lambda: [j for i in range(n) if (j := i) is not None]
print('Before:', f())
n = 10
print('After:', f())
