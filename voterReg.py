print("Welcome to the Voter Registeration App")

name = input("\nPlease enter you name: ").title().strip()
age = int(input("Please enter your age: "))

parties=["Republican","Democratic","Independent","Libertarian","Green"]

if age >=18:
    print(f"\nCongratulatins {name}! you are old enough to register yo vote ")
    print("Here is a list of political parties to join: ")
    for i in parties:
        print(f"- {i}")
    chosen = input("\nWhat party would you like to join: ").title().strip()
    print(f"\nCongratulations {name}! you have joined the {chosen} party!")
    if chosen=="Republican" or chosen=="Democratic":
        print("That is a major party")
    elif chosen=="Independence":
        print("You are Independent")
    else:
        print("That is not a major party")
else:
    print("You are not old enough to vote")