def login_required(func):
    def wrapper(user_logged_in):
        if user_logged_in:
            return func(user_logged_in)
        else:
            print("Access Denied. Please login.")
    return wrapper

@login_required
def dashboard(user_logged_in):
    print("Welcome to Dashboard")

dashboard(True)
dashboard(False)
