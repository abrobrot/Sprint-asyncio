import asyncio

async def before_after1():
    print("1")
    await asyncio.sleep(4)
    print("a")

async def before_after2():
    print("2")
    await asyncio.sleep(0)
    print("b")

async def before_after3():
    print("3")
    await asyncio.sleep(7)
    print("c")

async def main():
    await asyncio.gather(before_after1(), before_after2(), before_after3())

asyncio.run(main())
