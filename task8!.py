import asyncio


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
                self.task.cancel()
                break
            await asyncio.sleep(1)
            await self.task_r()


async def main():
    repeat_task = RepeatTask()
    repeat_task.task = asyncio.create_task(repeat_task.repeat())

    def cb(task):
            print("Выполнение закончено!")

    repeat_task.task.add_done_callback(cb)

    try:
        await repeat_task.task
    except asyncio.CancelledError:
        print("Успех!")


if __name__ == "__main__":
    asyncio.run(main())
