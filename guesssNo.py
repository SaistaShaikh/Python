import random

print("Welcome to the Guess My Number App")
name = input("\nHello! What is your name: ")

print(f"\nHello {name} I am thinking of a number between 1 to 20 ")
numb = random.randint(1,20)

for i in range(5):
    guess=int(input("\nTake a guess: "))
    if guess<numb:
        print("Your guess is too low")
    elif guess>numb:
        print("Your guess is too high")
    else:
        break

if guess ==numb:
    print(f"\nGood job! you guessed my number in {i+1} guesses")
else:
    print(f"\nGame over! The number I was thinking of was {numb}")

