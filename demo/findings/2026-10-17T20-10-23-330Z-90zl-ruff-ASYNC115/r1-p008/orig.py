import trio
from decimal import Decimal
async def main():
    vals = [0, 0.0, False, Decimal('0'), 0//1, (lambda: 0)()]
    for v in vals:
        try:
            await trio.sleep(v)
            print(f'{v!r}: slept')
        except Exception as e:
            print(f'{v!r}: {type(e).__name__}: {e}')
try:
    import asyncio
    asyncio.run(main())
except Exception as e:
    print(f'{type(e).__name__}: {e}')
