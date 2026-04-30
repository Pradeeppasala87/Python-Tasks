import numpy as np
nums = np.random.randint(1, 100, 10)
filtered = nums[nums%5 == 0]
sort = np.sort(filtered)
print(nums)
print(sort)
