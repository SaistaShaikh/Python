import cmath
#takes sqr root of negative nos

#welcome
print("Welcome to the Quadratic Solver App")

#giving information
print("\nA quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solution can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.")

count = int(input("\nHow many equations would you like to solve today: "))

#loop through and solve each eqn
for i in range(count):
    print(f"Solving equation #{i+1}")
    print("------------------------------------------------")
    a=float(input("Enter the value of a (coef of x^2):"))
    b=float(input("Enter the value of b (coef of x):"))
    c=float(input("Enter the value of c (coef):"))

    #solving quadratic formula
    x1 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)

    print(f"\nThe solution to {a}x^2 + {b}x + {c} = 0 are: ")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")

print("\nThank you....")
    