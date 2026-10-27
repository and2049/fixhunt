import asyncio
async def gen():
    for i in range(2):
        yield (i, i*2)
async def main():
    try:
        # This line triggers C402 but fix is invalid
        d = dict((k, v) for k, v in [(1,2),(3,4)])
        print('dict:', d)
    except Exception as e:
        print(type(e).__name__, str(e))
asyncio.run(main())
