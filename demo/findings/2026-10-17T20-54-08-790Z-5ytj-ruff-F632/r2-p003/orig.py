async def agen():
  yield 1
async def main():
  ag = agen()
  if ag is []:
    print('wrong')
  else:
    print('not list')
  try:
    await ag.__anext__()
  except StopAsyncIteration:
    print('done')
import asyncio
asyncio.run(main())
