def outer(**kwargs):
    def inner(*, limit=1):
        i = 0
        total = 0
        while 1:
            if i >= limit:
                break
            total += i
            i += 1
        return total
    return inner(**kwargs)

print(outer(limit=3))
