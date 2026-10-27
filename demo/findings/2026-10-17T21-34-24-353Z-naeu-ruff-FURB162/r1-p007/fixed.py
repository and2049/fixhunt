from datetime import datetime
import asyncio

async def gen():
    yield '2023-01-01T12:00:00Z'

async def main():
    async for s in gen():
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        print('async parsed:', dt.isoformat())
asyncio.run(main())
