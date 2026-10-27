async def aiter():
    yield 'hello'
    yield 'world'
async def consume():
    result = []
    async for item in aiter():
        result.append(item)
    return result
import asyncio
out = asyncio.run(consume())
print('result:', out)
print('length:', len(out))
