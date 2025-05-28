import asyncio


class RepeatTask:

    def __init__(self):
        self.counter = 0

    async def repeat(self, max_runs: int = 5):
        while True:
            self.counter += 1
            print("Программа выполнилась ", self.counter, "раз")
            if self.counter >= max_runs:
                return
            await asyncio.sleep(1)


async def main():
    repeat_task = RepeatTask()
    repeat_task.task = asyncio.create_task(repeat_task.repeat())

    def cb(task):
        print("Выполнение закончено!")

    repeat_task.task.add_done_callback(cb)
    await repeat_task.task


if __name__ == "__main__":
    asyncio.run(main())
