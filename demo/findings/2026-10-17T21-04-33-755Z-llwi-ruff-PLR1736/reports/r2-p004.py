lst = ['a', 'b', 'c']
for lst, lst in enumerate(lst):  # outer lst shadows inner? actually, first is index, second is element
    try:
        result = lst[lst]  # original: indexes the list with the element (string) -> error
    except Exception as e:
        print(f'{type(e).__name__}: {e}', end=' ')
