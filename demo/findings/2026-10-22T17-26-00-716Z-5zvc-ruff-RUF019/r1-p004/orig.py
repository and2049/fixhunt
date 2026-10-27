async def get_val(d, k):
    await asyncio.sleep(0)
    return d[k]
async def main():
    d = {'a': 1}
    if 'a' in d and await get_val(d, 'a'):
        print('truthy')
    else:
        print('falsy')
asyncio.run(main())
