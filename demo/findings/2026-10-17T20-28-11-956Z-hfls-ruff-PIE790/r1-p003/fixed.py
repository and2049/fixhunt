async def f():
    await asyncio.sleep(0)  # Requires import; use dummy awaitable
    class Awaitable:
        def __await__(self):
            yield
    await Awaitable()
    # Rule triggers: removable ellipsis after stmt
import asyncio
asyncio.run(f())
