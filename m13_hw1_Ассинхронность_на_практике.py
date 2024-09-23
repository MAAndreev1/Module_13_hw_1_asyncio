import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):
        await asyncio.sleep(5/power)
        print(f'Силач {name} поднял {i}')
    print(f'Силач {name} закончил соревнования')


async def main():
    task1 = asyncio.create_task(start_strongman('Пётор', 5))
    task2 = asyncio.create_task(start_strongman('Алексей', 10))
    task3 = asyncio.create_task(start_strongman('Степан', 15))
    await task1
    await task2
    await task3


asyncio.run(main())
