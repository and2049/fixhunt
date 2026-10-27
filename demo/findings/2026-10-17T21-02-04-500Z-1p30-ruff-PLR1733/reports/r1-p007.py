async def get_val(k):
    return k
class AwaitableDict(dict):
    def __getitem__(self, key):
        return get_val(key)
async def main():
    d = AwaitableDict({'x': 1})
    for k, v in d.items():
        x = await d[k]  # triggers PLR1733: would become await v — but v is int, not awaitable
import asyncio
result = asyncio.run(main())
