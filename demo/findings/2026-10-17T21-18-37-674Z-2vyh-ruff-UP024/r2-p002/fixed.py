async def foo():
    try:
        await bar()
    except OSError as e:
        print('caught IOError:', e)
    except OSError as e:
        print('caught OSError:', e)
async def bar():
    raise OSError('disk error')
import asyncio
asyncio.run(foo())
