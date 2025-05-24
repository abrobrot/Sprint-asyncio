import asyncio
from timeit import repeat


class RepeatTask:

    def __init__(self):
        self.counter = 0
        self.task = None

    async def task_r(self):
        self.counter += 1
        counter_max = self.counter
        print ("Программа выполнилась ", self.counter, "раз" )

    async def repeat(self, max_runs: int = 5):
        while True:
            if self.counter >= max_runs:
                if self.task:
                    self.task.cancel()
                break
            await self.task_r()
            await asyncio.sleep(0)


async def main():
    repeat_task = RepeatTask()
    task = asyncio.create_task(repeat_task.repeat())

    def cb(task_r):
            print("Выполнение закончено!")

    task.add_done_callback(cb)
    await task

if __name__ == "__main__":
    asyncio.run(main())
