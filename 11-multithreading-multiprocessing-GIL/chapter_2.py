# Global Interpreter Lock - GIL

# GIL threading

# import threading
# import time

# def brew_chai():
#     print(f"{threading.current_thread().name} started brewing...")
#     count = 0
#     for _ in range(100_000_000):
#         count += 1
#     print(f"{threading.current_thread().name} finished brewing...")

# thread1 = threading.Thread(target=brew_chai, name="Chai 1")
# thread2 = threading.Thread(target=brew_chai, name="Chai 2")


# start = time.time()

# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()

# end = time.time()

# print(f"Total time taken: {end-start:.2f} seconds")






# GIL multiprocessing

from multiprocessing import Process
import time

def crunch_number():
    print(f"Started counting...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Stopped counting...")



if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=crunch_number)
    p2 = Process(target=crunch_number)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time taken: {end-start:.2f} seconds")