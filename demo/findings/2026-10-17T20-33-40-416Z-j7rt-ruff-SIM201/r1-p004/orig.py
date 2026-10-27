async def get_x():
    print('get_x')
    return 1
async def get_y():
    print('get_y')
    return 2
async def main():
    x = await get_x()
    y = await get_y()
    if not x == y:   # Triggers SIM201
        print('unequal')
    else:
        print('equal')
asyncio.run(main())
