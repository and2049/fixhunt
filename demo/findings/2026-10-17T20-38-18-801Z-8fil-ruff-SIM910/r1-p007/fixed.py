d = {'name': 'Alice'}
for fmt in ['%s', '{}', f'{d.get("age")}']:
    try:
        if fmt == '%s':
            res = fmt % d.get('age')
        elif fmt == '{}':
            res = fmt.format(d.get('age'))
        else:
            res = eval(fmt)  # f-string
        print(repr(res))
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
