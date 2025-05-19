import asyncio


class Box:

    async def protection():
        print("защита")
        await asyncio.sleep(1)
    async def attack():
        print("удар")
        await asyncio.sleep(1)
    async def evasion():
        print("уклонение")
        await asyncio.sleep(1)

async def main():
    print(await Box.attack())

asyncio.run(main())
