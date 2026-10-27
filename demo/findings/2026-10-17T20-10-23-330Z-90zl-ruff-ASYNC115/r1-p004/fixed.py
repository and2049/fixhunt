import trio
from unittest.mock import patch
import trio.lowlevel
async def main():
    with patch('trio.sleep', return_value='mocked'):
        result = await trio.lowlevel.checkpoint()
        print('result:', repr(result))
try:
    import asyncio
    asyncio.run(main())
except Exception as e:
    print(f'{type(e).__name__}: {e}')
