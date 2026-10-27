outer = {'x': 10}
middle = {'y': 20}
for k, v in outer.items():          # outer k='x', v=10
    for k, v in middle.items():       # inner k='y', v=20 (shadows outer)
            x = outer[k]              # triggers PLR1733: outer['y']?? -> KeyError
