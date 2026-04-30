def even_generator():
    n = 2
    while True:
        yield n
        n += 2

gen = even_generator()

for _ in range(5):
    print(next(gen))
