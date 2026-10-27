class DictLike:
    def __init__(self, d):
        self.d = d
        self.call_count = 0
    def __aiter__(self):
        return self
    async def __anext__(self):
        if self.call_count >= 2:
            raise StopAsyncIteration
        self.call_count += 1
        return list(self.d.items())[self.call_count - 1]
    def __bool__(self):
        return len(self.d) > 0

async def test():
    d = DictLike({'x': 10})
    result = []
    # Rule triggers: for k, v in d: (but d is not a dict, it's DictLike)
    # However, the rule only fires on dict variables — so we make d a dict but wrap access
    # Instead: use a dict but make __bool__ matter via conditional break
    pass

# Let's refactor: use real dict but rely on truthiness to control loop entry
d = {'a': 1}
if d:  # truthiness check
    result = []
    for k, v in d:  # <- TRIGGER
        result.append((k, v))
        if not d:  # mutate to falsy
            d.clear()
    print('result:', result, 'dict after:', d)
else:
    print('skipped')
