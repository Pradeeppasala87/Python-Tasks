import numpy as gt

random  = gt.random.randint(100, size=8)
normalize = random * 100
filtered = normalize[normalize > 50]
data = gt.sort(filtered)
print(random)
print(normalize)
print(filtered)
print(data)
