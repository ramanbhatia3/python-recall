# multiprocess with queue and value

# process 1

import threading
import time

# def cpu_heavy():
#     print("Crunching some numbers")
#     total = 0
#     for i in range(10**7):
#         total += i
#     print("DONE")

# start = time.time()

# threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]
# [t.start() for t in threads]
# [t.join() for t in threads]

# end = time.time()

# print(f"Time taken: {end-start:.2f} seconds")




# process 2

from multiprocessing import Process

def cpu_heavy():
    print("Crunching some numbers")
    total = 0
    for i in range(10**7):
        total += i
    print("DONE")

if __name__ == "__main__":
    start = time.time()

    processes = [Process(target=cpu_heavy) for _ in range(2)]
    [t.start() for t in processes]
    [t.join() for t in processes]

    end = time.time()

    print(f"Time taken: {end-start:.2f} seconds")