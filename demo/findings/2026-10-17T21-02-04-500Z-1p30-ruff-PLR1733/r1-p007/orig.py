async def get_val(k):
    await asyncio.sleep(0.001)
    return k
class AwaitableDict(dict):
    def __getitem__(self, key):
        return get_val(key)
async def main():
    d = AwaitableDict({'x': 1})
    trace = []
    for k, v in d.items():
        trace.append('before')
        x = await d[k]  # triggers PLR1733: would become await v — but v is int, not awaitable
        trace.append(('after', x))
    return trace
import asyncio
result = asyncio.run(main())
print('result:', result)
