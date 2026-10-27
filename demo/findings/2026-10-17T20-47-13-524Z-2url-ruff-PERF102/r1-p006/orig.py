def h(*, kw, d={'x': 1}):
    for k, _ in d.items():
        kw.append(k)
    return kw
print(h(kw=[]))
