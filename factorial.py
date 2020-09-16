import math
#welcome
print("Welcome to the Factorial Calculator App")

#get user input
no=int(input("What input no would you like to compute factorial of: "))

#displaying the mathematical relation
print(f"{no}! = ", end="")
for i in range(1,no):
    print(f"{i}*",end="")
print(no)

#using math library
fact = math.factorial(no)
print("\nHere is the result from the math library")
print(f"The factorial of {no} is {fact}")

#using own algorithm
fact=1
for i in range(1,no+1):
    fact=fact*i
print("\nHere is the result from my own library")
print(f"The factorial of {no} is {fact}")

#summary
print(f"\nIt is shown twice that {no}! is {fact}")

