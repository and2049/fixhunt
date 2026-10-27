import trio
# This is a comment before
async def main():
    # Comment before await
    await trio.sleep(0)  # Inline comment
    # Comment after await
    print('done')
# Comment after function
trio.run(main())
