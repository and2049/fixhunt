async def gen():
    for s in ['0b1', '0b10']:
        yield int(s[2:], 2)
async def main():
    result = [x async for x in gen()]
    print(result)
import asyncio
asyncio.run(main())
