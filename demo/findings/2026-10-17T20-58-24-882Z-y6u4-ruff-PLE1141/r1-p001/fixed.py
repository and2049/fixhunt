async def main():
    d = {'a': 1}
    result = []
    # Rule triggers here: for k, v in d: -> should become for k, v in d.items():
    async for k, v in d:
        result.append((k, v))
        await asyncio.sleep(0)
    print('result:', result)
asyncio.run(main())
