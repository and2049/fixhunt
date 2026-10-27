import trio
import trio.lowlevel
async def main():
    with open('test.bin', 'wb') as f:
        try:
            f.write(b'before')
            await trio.lowlevel.checkpoint()
            f.write(b'after')
        except Exception as e:
            print(f'{type(e).__name__}: {e}')
        finally:
            f.seek(0)
            print('read:', f.read())
import asyncio
import os
asyncio.run(main())
os.remove('test.bin')
