cart = []
prices = []

while True:
    try:
        item = input("Enter item (or stop): ")
        if item == "stop":
            break

        price = float(input("Enter price: "))

        cart.append(item)
        prices.append(price)

    except:
        print("Invalid input!")


cart = list(set(cart))

total = 0
for p in prices:
    total += p

print("Cart:", cart)
print("Total:", total)
