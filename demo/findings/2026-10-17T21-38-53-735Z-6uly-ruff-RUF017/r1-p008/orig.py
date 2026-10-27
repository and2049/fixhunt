def make_gen():
    print('  Generator started')
    for i in range(3):
        print(f'  Yielding [{i}, {i+1}]')
        yield [i, i+1]
    print('  Generator ended')

print('First sum:')
gen = make_gen()
result1 = sum(gen, [])
print('Result:', result1)

print('\nSecond sum (same generator):')
gen2 = make_gen()  # new generator
result2 = sum(gen2, [])
print('Result:', result2)

print('\nManual reduce for comparison:')
from functools import reduce
import operator
gen3 = make_gen()
result3 = reduce(operator.iadd, gen3, [])
print('Reduce result:', result3)
