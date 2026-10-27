async def async_gen():
    for i in range(3):
        yield i

async def main():
    # This would be invalid if rewritten: set(await x for x in async_gen()) -> {
    # But rule does not fire on async generators, so this is safe.
    # We show that the code runs and the rule is silent.
    result = set()
    async for x in async_gen():
        result.add(x)
    print('async set:', result)

import asyncio
asyncio.run(main())
