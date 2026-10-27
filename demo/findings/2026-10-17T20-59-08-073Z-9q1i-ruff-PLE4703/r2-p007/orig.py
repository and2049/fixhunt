async def worker(s):
    for x in s:
        await asyncio.sleep(0)
        s.add(x + 10)
async def main():
    s = {1, 2}
    await worker(s)
    print('result:', sorted(s))
asyncio.run(main())
