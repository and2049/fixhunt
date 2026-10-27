async def agen():
    for i in range(3):
        yield i
async def main():
    result = [i async for i in agen()]
    print(result)
import asyncio
asyncio.run(main())
