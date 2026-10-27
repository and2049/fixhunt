async def gen():
    yield 1
    await asyncio.sleep(0)
async def main():
    async for v in gen():
        print(v)
asyncio.run(main())
