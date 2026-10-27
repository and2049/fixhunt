import trio
async def main():
    await trio.sleep(0)
    print('before checkpoint')
    await trio.lowlevel.checkpoint()  # This line will fail if not imported
    print('after checkpoint')
trio.run(main())
