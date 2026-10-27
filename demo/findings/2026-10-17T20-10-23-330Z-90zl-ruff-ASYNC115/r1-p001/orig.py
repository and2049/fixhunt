# -*- coding: utf-8 -*-
import trio
async def main():
    x = 0
    y = [
        await 	 trio.sleep( 0 )  # tab and space after comma
        if False else None,
    ]
    print('y[0]:', y[0])
try:
    import asyncio
    asyncio.run(main())
except Exception as e:
    print(f'{type(e).__name__}: {e}')
