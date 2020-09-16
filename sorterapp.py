#grade sorter app

print("Welcome to the Grade Sorter app")

#initialize list and get user input
grades=[]
grade=int(input("\nWhat is your first grade (0-100):"))
grades.append(grade)
grade=int(input("What is your second grade (0-100):"))
grades.append(grade)
grade=int(input("What is your third grade (0-100):"))
grades.append(grade)
grade=int(input("What is your fourth grade (0-100):"))
grades.append(grade)

print(f"\nYour grades are {grades}")

#sort from highest to lowest
grades.sort(reverse=True)
print(f"\nYour grades from highest to lowest are: {grades}")

#removing lowest two grades
print("\nThe lowest two grades will now be dropped")
print(f"Removed grade: {grades.pop()}")
print(f"Removed grade: {grades.pop()}")

#print remaining grades
print(f"\nYour remaining grades are: {grades}")
print(f"Your highest grade is {grades[0]}")

print("\nNice work!")

