#Welcome msg
print("Welcome to the Average Calculator App")

#Get user input
name=input("What is your name: ").title().strip()
no=int(input("How many grades would you like to enter: "))

#get user grades
grades=[]
for i in range(no):
    grades.append(int(input("Enter grade: ")))

#sorting grades and print
grades.sort(reverse=True)
print(f"\nGrades highest to lowest: ")
for i in grades:
    print(i)

#avg cal
average=sum(grades)/len(grades)
average=round(average,2)

#summary
print(f"\n {name}'s Grade Summary:")
print(f"Total no of grades: {len(grades)}")
print(f"Highest Grade: {max(grades)}")
print(f"Lowest Grade: {min(grades)}")
print(f"Average: {average}")

#get user's desired avg and cal what they need next
desired_avg=float(input("\nWhat is your desired avg:"))
grade_req = desired_avg*(len(grades)+1) - sum(grades)
grade_req = round(grade_req,2)

print(f"{name} you will need to get a {grade_req} on your next assignment to earn a {desired_avg}")