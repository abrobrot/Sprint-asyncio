import asyncio
from asyncio import create_task


async def time_two():
    await asyncio.sleep(5)

async def time_three():
    await asyncio.sleep(1)

async def time_four():
    await asyncio.sleep(7)

async def main():
    task123 = [create_task(time_two()),
               create_task(time_three()),
               create_task(time_four())]
    done, pending = await asyncio.wait(task123, return_when=asyncio.FIRST_COMPLETED)
    for task in done:
        print(f"Первой завершилась: {task.get_name()}")

        for task in pending:
            task.cancel()

        await asyncio.gather(*pending, return_exceptions=True)

asyncio.run(main())
