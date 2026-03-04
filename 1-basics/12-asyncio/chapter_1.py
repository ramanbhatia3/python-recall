# asyncio, event loop, coroutines and await


# async def - declare a coroutine ( special function that can be paused )

# await - pauses execution until the result is ready

# asyncio - built in python library

# event loop - the engine that runs and schedule code routines in python

import asyncio
import time

# async def brew_chai():
#     print("Brewing chai...")
#     await asyncio.sleep(2)
#     print("Chai is ready")

# asyncio.run(brew_chai())



# async def brew(name):
#     print(f"Brewing {name}...")
#     await asyncio.sleep(2)
#     # time.sleep(2)
#     print(f"{name} is ready")

# async def main():
#     await asyncio.gather(
#         brew("Masala Chai"),
#         brew("Ginger Chai"),
#         brew("Green Chai"),
#     )

# asyncio.run(main())






import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with Status code: {response.status}")
        
async def main():
    urls = [
        "https://www.google.com",
        "https://www.facebook.com",
        "https://www.linkedin.com",
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())


# blocking vs non-blocking

# blocking - time.sleep(2)

# non-blocking - await asyncio.sleep(2)