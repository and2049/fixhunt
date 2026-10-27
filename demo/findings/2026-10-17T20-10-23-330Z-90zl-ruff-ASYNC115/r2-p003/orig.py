import trio as t
async def main():
    await t.sleep(0)
    print('aliased ok')
trio.run(main())
