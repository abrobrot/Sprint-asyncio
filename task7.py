import asyncio
import aiohttp
from datetime import datetime


async def filter_counter(session, url):
    start_time = datetime.now()
    try:
        async with session.get(url) as response:
            if response.status == 200:
                end_time = datetime.now()
                ping_time = (end_time - start_time).total_seconds() * 1000
                print(f"{url} - Успешно. Время отклика: {ping_time:.2f} мс")
            else:
                print(f"{url} - Ошибка {response.status}")
    except Exception as e:
        print(f"{url} - Ошибка: {str(e)}")

async def ping_sites():
    sites = ["https://google.com",
        "https://meet.google.com/landing",
        "https://github.com",
        "https://web.telegram.org",
        "https://vk.coma"
        ]

    async with aiohttp.ClientSession() as session:
        tasks = [filter_counter(session, url) for url in sites]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(ping_sites())
