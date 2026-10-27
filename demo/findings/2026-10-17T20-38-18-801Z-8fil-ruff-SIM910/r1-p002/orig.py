data = {'x': 10}
result = [(v := data.get(k, None)) for k in ['x', 'y'] if v is not None]
print(result)
