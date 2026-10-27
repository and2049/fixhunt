outer = {'x': 10}
middle = {'y': 20}
inner = [1, 2]
trace = []
for k, v in outer.items():          # outer k='x', v=10
    for k, v in middle.items():       # inner k='y', v=20 (shadows outer)
        for _ in inner:
            trace.append((k, v))      # k,y v,20 from middle
            x = v              # triggers PLR1733: outer['y']?? -> KeyError
            trace.append(('got', x))
print('trace:', trace)
