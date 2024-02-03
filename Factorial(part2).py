import math
factorial_number = []
number = int(input("Enter your number: "))
for i in range(1000):
    x = math.factorial(i)
    factorial_number.append(x)

if number in factorial_number:
    print("Yes")
else:
    print("No")

