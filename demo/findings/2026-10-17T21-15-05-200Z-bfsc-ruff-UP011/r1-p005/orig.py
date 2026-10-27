import functools
@functools.lru_cache()
async def fetch():
  await _dummy()
  return 99
async def _dummy(): pass
import asyncio
result = asyncio.run(fetch())
print(result)
