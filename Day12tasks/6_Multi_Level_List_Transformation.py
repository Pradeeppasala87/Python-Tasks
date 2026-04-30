data = [[1, 2, 3], [4, 5], [6]]

flattened = [item for sublist in data for item in sublist]
print(flattened)
even_squares = [x**2 for x in flattened if x % 2 == 0]
print(even_squares)
