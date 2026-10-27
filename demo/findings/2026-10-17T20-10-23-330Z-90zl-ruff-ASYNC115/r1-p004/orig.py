import trio
from unittest.mock import patch
async def main():
    with patch('trio.sleep', return_value='mocked'):
        result = await trio.sleep(0)
        print('result:', repr(result))
try:
    import asyncio
    asyncio.run(main())
except Exception as e:
    print(f'{type(e).__name__}: {e}')
