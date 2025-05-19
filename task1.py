import asyncio


async def print_number():
    while True:
        print (1)
        await asyncio.sleep(1)

async def print_letter():
    while True:
        print ("a")
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(print_number())
    task2 = asyncio.create_task(print_letter())
    await asyncio.sleep(4)
    task1.cancel()
    task2.cancel()

    try:
        await task1
        await task2
    except asyncio.CancelledError:print("Задачи отменены!")

asyncio.run(main())
