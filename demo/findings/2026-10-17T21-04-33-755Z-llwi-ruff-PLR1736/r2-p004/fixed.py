lst = ['a', 'b', 'c']
for lst, lst in enumerate(lst):  # outer lst shadows inner? actually, first is index, second is element
    # Rule sees: lst[lst] -> wants to replace with lst (element), but lst is now element, not list
    # So original: lst[index] -> element at index
    # Fix: lst (element) -> which is a string, not indexable -> TypeError
    try:
        result = lst  # original: indexes the list with the element (string) -> error
    except Exception as e:
        print(f'{type(e).__name__}: {e}', end=' ')
print()
