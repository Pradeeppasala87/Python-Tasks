
products = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5
}


categories = {"Stationery"}

# List for cart items (each item as tuple: (product_name, quantity))
cart = []

# Tuple for product details (example: immutable structure)
product_details = (
    ("Pen", 10),
    ("Notebook", 50),
    ("Pencil", 5)
)


# Recursive function to calculate total bill
def calculate_total(cart_list):
    if len(cart_list) == 0:
        return 0
    item = cart_list[0]
    try:
        price = products[item[0]]
        return (price * item[1]) + calculate_total(cart_list[1:])
    except TypeError:
        raise TypeError


# Function to display products
def display_products():
    print("Available Products:")
    for name, price in products.items():
        print(f"{name} : {price}")


# Function to add item to cart
def add_to_cart():
    try:
        name = input("Enter product name: ")

        if name not in products:
            raise NameError

        qty = input("Enter quantity: ")

        if not qty.isdigit():
            raise ValueError

        qty = int(qty)

        cart.append((name, qty))
        print("Item added to cart successfully.")

    except NameError:
        print("Product not found in store.")

    except ValueError:
        print("Invalid quantity! Please enter a number.")


# Function to view total bill
def view_total():
    try:
        if not cart:
            print("Cart is empty.")
            return

        print("Items in Cart:")
        for item in cart:
            print(f"{item[0]} x {item[1]}")

        total = calculate_total(cart)

        # Artificial check to demonstrate ZeroDivisionError handling
        if len(cart) == 0:
            total = total / 0

        print("Total Bill:", total)

    except TypeError:
        print("Cart data type error.")

    except ZeroDivisionError:
        print("Calculation error: division by zero.")


# Menu-driven program
def main():
    while True:
        print("\n1. Display Products")
        print("2. Add Item to Cart")
        print("3. View Total Bill")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            display_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            view_total()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


# Run program
main()
