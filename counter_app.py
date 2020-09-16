#Letter counter app

print("Welcome to the Letter Counter App")

#Get user input
name = input("\nWhat is your name: ").title().strip()
print("Hello, " + name + " ! ")

print("I'll count the number of times specific letter occurs in a message")

message = input("\nEnter your message: ")
letter = input("\nEnter the letter you want to count the occurence of: ")


#standardize to lower case
message = message.lower()
letter = letter.lower()

#count and display
letter_count = message.count(letter)
print(f"{name} your message has {letter_count} {letter}'s in it")


