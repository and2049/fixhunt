lst = [5, 6, 7]
print('List comprehension with walrus:')
squares = [ (n := x) * n for x in lst if bin(n := x).count('1') == 2 ]
print(f'  Result: {squares}, final n: {n}')
print('
Generator expression capture:')
gen = (bin(n := x).count('1') for x in lst)
first = next(gen)
print(f'  First from gen: {first}, n after: {n}')
second = next(gen)
print(f'  Second from gen: {second}, n after: {n}')
print('
Lambda late-binding:')
funcs = [lambda x=x: bin(n := x).count('1') for x in lst]
for f in funcs:
    print(f'  Lambda result: {f()}')
