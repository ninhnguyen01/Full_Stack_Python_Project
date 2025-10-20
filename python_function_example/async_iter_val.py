# Return an asynchronous iterator 

import asyncio

async def async_gen():
    yield 6
    yield 2
    yield 6
    yield "Welcome to San Gabriel Valley!"

async def main():
    async_iter = aiter(async_gen())

    async for i in async_iter:
        print(i)

asyncio.run(main())      