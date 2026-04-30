def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
print("Sum of list:", sum_list(numbers))
