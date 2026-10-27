def gen_lists():
    yield [1, 2]
    yield (3, 4)  # tuple, not list
    yield {5, 6}  # set, not list

print('Input:')
for item in gen_lists():
    print(f'  {item} ({type(item).__name__})')

try:
    result = sum(gen_lists(), [])
    print('sum result:', result, type(result))
except Exception as e:
    print('sum error:', type(e).__name__, str(e))

# Reset generator
print('\nReduce form:')
from functools import reduce
import operator
result2 = reduce(operator.iadd, gen_lists(), [])
print('reduce result:', result2, type(result2))
