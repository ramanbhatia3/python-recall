# auth decorator

from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access Denied: Admins ONLY!!")
            return None # (optional line)
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_inventory(role):
    print("Access Granted!")

access_inventory("user")
access_inventory("admin")