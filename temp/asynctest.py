import asyncio
import time


async def sleep(ti):
    await asyncio.sleep(ti)


async def p(c, t):
    for i in range(100) :
        print(c)
        await sleep(t)


async def main():
    start = time.time()

    task1 = asyncio.create_task(p("a", 1))
    task2 = asyncio.create_task(p("c", 0.5))

    await task1
    await task2

    



asyncio.run(main())