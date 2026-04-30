n = int(input("How many items? "))

with open("grocery.txt", "w") as file:
    for i in range(n):
        item = input("Enter item: ")
        file.write(item + "\n")

print("Grocery list saved successfully!")
