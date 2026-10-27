d = {'name': 'Alice'}
for fmt in ['%s', '{}', f'{d.get("age", None)}']:
    try:
        if fmt == '%s':
            res = fmt % d.get('age', None)
        elif fmt == '{}':
            res = fmt.format(d.get('age', None))
        else:
            res = eval(fmt)  # f-string
        print(repr(res))
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
