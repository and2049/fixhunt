import asyncio
async def afunc():
    await asyncio.sleep(0.001)
    return 'done'
async def main():
    r1 = ' '.join((await afunc(), await afunc()))
    r2 = f'{await afunc()} {await afunc()}'
    print(f'{r1}|{r2}')
asyncio.run(main())
