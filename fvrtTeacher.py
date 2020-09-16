#Welcome msg
print("Welcome to the Favourite Teacher Program")

teachers=[]

#taking user input
teachers.append(input("Who is your first favourite teacher: ").title())
teachers.append(input("Who is your second favourite teacher: ").title())
teachers.append(input("Who is your third favourite teacher: ").title())
teachers.append(input("Who is your fourth favourite teacher: ").title())


#displaying summary of list
print(f"\nYour favourite teachers ranked are: {teachers}")
print(f"Your favourite teachers alphabetically are: {sorted(teachers)}")
print(f"Your favourite teachers in reverse alphabetical order are: {sorted(teachers,reverse=True)}")
print(f"\nYour top two favourite teachers are: {teachers[0]} {teachers[1]}")
print(f"Your next two favourite teachers are: {teachers[2]} {teachers[3]}")
print(f"Your last favourite teacher is: {teachers[-1]}")
teacher_length=len(teachers)
print(f"You have a total of {teacher_length} favourite teachers")

#Remove one fav teacher and insert another
teachers.insert(0,input(f"Oops! {teachers[0]} is no longer your first favourite teacher. Who is your new favourite teacher:").title())

#summary
print(f"\nYour favourite teachers ranked are: {teachers}")
print(f"Your favourite teachers alphabetically are: {sorted(teachers)}")
print(f"Your favourite teachers in reverse alphabetical order are: {sorted(teachers,reverse=True)}")
print(f"\nYour top two favourite teachers are: {teachers[0]} {teachers[1]}")
print(f"Your next two favourite teachers are: {teachers[2]} {teachers[3]}")
print(f"Your last favourite teacher is: {teachers[-1]}")
teacher_length=len(teachers)
print(f"You have a total of {teacher_length} favourite teachers")

#remove a specific teacher
teachers.remove(input("You decided you no longer like a teacher. Which teacher would you like to remove: ").title())

#summary
print(f"\nYour favourite teachers ranked are: {teachers}")
print(f"Your favourite teachers alphabetically are: {sorted(teachers)}")
print(f"Your favourite teachers in reverse alphabetical order are: {sorted(teachers,reverse=True)}")
print(f"\nYour top two favourite teachers are: {teachers[0]} {teachers[1]}")
print(f"Your next two favourite teachers are: {teachers[2]} {teachers[3]}")
print(f"Your last favourite teacher is: {teachers[-1]}")
teacher_length=len(teachers)
print(f"You have a total of {teacher_length} favourite teachers")


