import random

nums = []

for i in range(10):
    nums.append(random.randint(1, 50))

even = 0
odd = 0

for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

unique = set(nums)

print("Numbers:", nums)
print("Even:", even)
print("Odd:", odd)
print("Unique:", unique)
