def process(val):
    if val:
        return val * 2
    else:
        # TODO: handle zero case
        pass
print(process(5))
print(process(0))  # Should print None, but comment loss may hint at refactoring risk
