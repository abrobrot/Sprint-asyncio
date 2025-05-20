import asyncio

async def before_after():
    print("Уснул")
    await asyncio.sleep(1)
    print("Проснулся")

asyncio.run(before_after())
