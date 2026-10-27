def f(a=[]):
    if not a == []:
        a.append(99)
    return a

print(f'first: {f()}')
print(f'second: {f()}')
print(f'third: {f()}')

# reset by redefining
def f2(a=[]):
    if a != []:
        a.append(99)
    return a

print(f'first2: {f2()}')
print(f'second2: {f2()}')
print(f'third2: {f2()}')
