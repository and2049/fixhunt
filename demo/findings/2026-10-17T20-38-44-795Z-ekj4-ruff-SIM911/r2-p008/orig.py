async def gen():
    d = {'a': 1, 'b': 2}
    for k, v in zip(d.keys(), d.values()):
        yield k, v
import asyncio
async def main():
    result = [pair async for pair in gen()]
    print(result)
asyncio.run(main())
