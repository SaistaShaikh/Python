import math
print("Welcome to the right triangle solver")

#user input
side_a = float(input("\nWhat is the first leg of your triangle: "))
side_b = float(input("What is the second leg of the triangle: "))

#calculations
side_c = math.sqrt((side_a**2 + side_b**2))
side_c = round(side_c,3)

area = 0.5*side_a*side_b
area = round(area,3)

print(f"\nFor a triangle with legs {side_a} and {side_b} hyp is {side_c} and area is {area}")
