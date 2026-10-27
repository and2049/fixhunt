name = 'World'
extra = 42
template = 'Hello %(name)s'
data = {'name': name, 'extra': extra}
try:
    percent_result = template % data
    format_result = template.format_map(data)
    f_result = f'Hello {name}'
    print('%:', percent_result)
    print('.format_map:', format_result)
    print('f-string:', f_result)
except Exception as e:
    print('Error:', type(e).__name__, str(e))
