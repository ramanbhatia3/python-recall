# threads and locks

# thread1

import threading
import time

def boil_milk():
    print(f"Boiling Milk...")
    time.sleep(2)
    print(f"Milk Boiled...")

def toast_bun():
    print(f"Toasting Bun...")
    time.sleep(3)
    print(f"Bun Toasted...")

start = time.time()

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Breakfast in ready in {end-start:.2f} seconds")


# thread2

def prepare_chai(type_, wait_time):
    print(f"{type_} chai brewing...")
    time.sleep(wait_time)
    print(f"{type_} chai ready...")

new_start = time.time()

t3 = threading.Thread(target=prepare_chai, args = ("Masala",2))
t4 = threading.Thread(target=prepare_chai, args = ("Ginger",3))

t3.start()
t4.start()

t3.join()
t4.join()

new_end = time.time()

print(f"Chais ready in {end-start:.2f} seconds")