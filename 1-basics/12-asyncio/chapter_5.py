# daemon vs non-daemon threads

# daemon

# daemon threads are the background threads that are killed when the main thread exits. These are used for tasks that are not critical to the program's execution and can be safely terminated when the main thread finishes. Examples include logging, monitoring, or background cleanup tasks.



# import threading
# import time

# def monitoring_tea_temp():
#     while True:
#         print("Monitoring tea temperature...")
#         time.sleep(2)

# t = threading.Thread(target=monitoring_tea_temp, daemon=True)
# t.start()

# print("Main program done!")

# non-daemon

#  Non-daemon threads are the foreground threads that keep the program running until they complete their task. These threads are essential for the program's execution, and the main thread will wait for them to finish before exiting. Examples include tasks that perform critical operations, such as processing data, handling user input, or performing calculations.


import threading
import time

def monitoring_tea_temp():
    while True:
        print("Monitoring tea temperature...")
        time.sleep(2)

t = threading.Thread(target=monitoring_tea_temp)
t.start()

print("Main program done!")