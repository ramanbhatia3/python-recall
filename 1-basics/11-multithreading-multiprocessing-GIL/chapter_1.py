# concurrency

# |
# |      ---
# |    --- ---
# |  ---     ---
# |---         ---
# |__________________


# parallelism

# |
# |
# |_______________
# |_______________
# |_______________
# |
# |___________________

# concurrency           parallelism

# threading.Thread      multiprocessing.Process
# asyncio               concurrent.futures.ProcessPoolExecutor



# threading

import threading
import time

def take_orders():
    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(2)


def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)


# create threads

order_thread = threading.Thread(target=take_orders)

brew_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start()

# wait for both to finish
order_thread.join()
brew_thread.join()

print("All orders taken and chais brewed")




# multiprocessing

from multiprocessing import Process
import time

def brew_coffee(name):
    print(f"{name} coffee served!")
    time.sleep(3)
    print("Do you like the coffee?")

if __name__ == "__main__":
    coffee_makers = [
        Process(target=brew_coffee, args=(f"Coffee Maker #{i+1}", ))
        for i in range(3)
    ]

    # start all process
    for p in coffee_makers:
        p.start()

    # wait for all to complete
    for p in coffee_makers:
        p.join()

    print("Coffees Served!")