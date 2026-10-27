async def agen():
    yield 1
    yield 2
async def main():
    try:
        for x in list(agen()):
            print(x)
    except TypeError as e:
        print('expected:', type(e).__name__, e)
import asyncio
asyncio.run(main())
