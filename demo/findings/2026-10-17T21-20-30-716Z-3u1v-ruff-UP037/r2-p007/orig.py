def make_checker():
    return lambda: "int"  # return annotation

checker = make_checker()
try:
    ann = checker.__annotations__['return']
    print(f'Lambda return annotation: {repr(ann)}')
    if isinstance(ann, str):
        print('Annotation is string, safe to eval later')
    else:
        print('Annotation resolved, assuming type in scope')
except KeyError:
    print('No return annotation')
