import asyncio


class Repeat_task:
    def __init__(self):
        self.counter = 0
        self.task = None

    async def task_r(self):
        self.counter += 1
        print ("Программа выполнилась ", self.counter, "раз" )

    async def repeat(self, max_runs: int = 5):
        while True:
            if self.counter >= max_runs:
                print ("Выполнение закончено")
                if self.task:
                    self.task.cancel
                break
            await self.task_r()
            await asyncio.sleep(2)
async def main():
    repeat_task = Repeat_task()
    repeat_task.task = asyncio.create_task(repeat_task.repeat())

    try:
            await repeat_task.task
    except asyncio.CancelledError:
            print("Задача была отменена.")

asyncio.run(main())
