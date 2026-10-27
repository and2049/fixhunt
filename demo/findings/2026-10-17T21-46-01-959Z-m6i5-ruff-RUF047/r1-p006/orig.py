async def async_fn():
    await asyncio.sleep(0.01)
    if True:
        return 42
    else:
        pass
import asyncio
async def main():
    result = await async_fn()
    print("Result:", result)
asyncio.run(main())
