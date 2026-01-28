import asyncio

async def say(phrase, seconds):
    print(phrase)
    await asyncio.sleep(seconds)

async def wicked():
    task_1 = asyncio.create_task(say("Surrender,", 2))
    task_2 = asyncio.create_task(say("Dorothy!", 0))
    await task_1
    await task_2

asyncio.run(wicked())

# Synchronous and asynchronous code can coexist in the same program. 
# Just remember to put async before the def, and await before the call of your asynchronous function.
