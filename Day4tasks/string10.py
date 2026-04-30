user = input("Enter a string: ")
result = ""

for char in user:
    if char not in result:
        result += char

print("String after removing duplicates:", result)
