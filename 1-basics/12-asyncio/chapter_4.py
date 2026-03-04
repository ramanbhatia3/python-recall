# logger

import asyncio
import threading
import time

def backhground_worker():
    while True:
        time.sleep(1)
        print(f"Logging the system health")

async def fetch_orders():
    await asyncio.sleep(2)
    print("Orders Fetched")

threading.Thread(target=backhground_worker, daemon=True).start()

asyncio.run(fetch_orders())