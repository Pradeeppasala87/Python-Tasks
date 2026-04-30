def number_generator(n):
    for i in range(1, n + 1):
        yield i

for num in number_generator(5):
    print(num)
