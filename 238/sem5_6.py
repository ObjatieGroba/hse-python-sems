import asyncio
import time
import aiohttp

async def func():
    await asyncio.sleep(1)
    # async with aiohttp.ClientSession() as session:
    #     async with session.get('http://python.org') as response:
    #         html = await response.text()
    #         print(html)
    return 1

async def main():
    return await asyncio.gather(func(), func())

async def dunc():
    yield 1

start = time.time()
print(asyncio.run(main()))
print(time.time() - start)
