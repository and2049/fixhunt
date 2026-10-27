import asyncio
async def get_val(name, val):
    print(f'{name} computed')
    return val
async def main():
    a = await get_val('a', False)
    b = await get_val('b', True)
    c = await get_val('c', True)
    res = a or (b and c)
    print(res)
asyncio.run(main())
