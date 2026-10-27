async def gen():
  yield 1
async def main():
  async for v in gen():
    print(v)
import asyncio
asyncio.run(main())
