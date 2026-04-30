users = {"admin": "admin", "user": "user"}

def check_role(func):
    def wrapper(role):
        if role == "admin":
            func(role)
        else:
            print("Access denied")
    return wrapper

@check_role
def dashboard(role):
    print("Welcome admin")

dashboard("admin")
dashboard("user")
