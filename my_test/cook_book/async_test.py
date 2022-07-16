from asyncio import run
import time

async def async_function():
    time.sleep(1)
    return 1


async def await_coroutine():
    result = await async_function()
    print(result)


run(await_coroutine())
