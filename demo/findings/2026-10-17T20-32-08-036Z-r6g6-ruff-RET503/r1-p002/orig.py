async def g():
    raise ValueError('fail')
async def f():
    await g()
    return 42
import asyncio
try:
    asyncio.run(f())
except Exception as e:
    print(type(e).__name__, str(e))
