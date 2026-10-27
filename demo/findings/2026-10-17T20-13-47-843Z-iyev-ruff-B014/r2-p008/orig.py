async def maybe_fail():
    await asyncio.sleep(0)  # yield control
    raise ValueError('async error')

async def main():
    try:
        await maybe_fail()
    except (ValueError, Exception):  # ValueError subsumed by Exception
        print('Caught ValueError')
        return 42
    finally:
        print('Finally in async')

import asyncio
result = asyncio.run(main())
print('Result:', result)
