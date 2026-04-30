num = int(input("Enter a number: "))
temp = num
sum_fact = 0

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

while temp > 0:
    digit = temp % 10
    sum_fact += factorial(digit)
    temp //= 10

if sum_fact == num:
    print(num, "is a Strong number")
else:
    print(num, "is not a Strong number")
