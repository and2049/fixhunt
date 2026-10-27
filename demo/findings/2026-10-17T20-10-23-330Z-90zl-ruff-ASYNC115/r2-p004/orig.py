from trio import sleep
async def main():
    await sleep(0)
    print('from import ok')
trio.run(main())
