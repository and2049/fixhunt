import trio
async def wrapper(*args, **kwargs):
    return await trio.sleep(*args, **kwargs)
async def main():
    result = await wrapper(0)
    print('forwarded:', result)
async def posonly(/, delay):
    return await trio.sleep(delay)
async def main2():
    r = await posonly(0)
    print('posonly:', r)
async def kwonly(*, delay):
    return await trio.sleep(delay)
async def main3():
    r = await kwonly(delay=0)
    print('kwonly:', r)
asyncio.run(main())
asyncio.run(main2())
asyncio.run(main3())
