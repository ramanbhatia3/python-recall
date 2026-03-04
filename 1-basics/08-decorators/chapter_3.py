# logging decorator

from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@log_activity
def call_me(name, relation="Bhai"):
    print(f"Calling {name} {relation}!")

call_me("Mohit")