import random

#welcome
print("Welcome to the Coin Toss app")
print("\nI will flip a coin a set number of times")

#user input
flip_number=int(input("\nHow many times would you like me to flip the coin: "))
choice=input("Would you like to see the result of each flip (y/n): ")

print("\nFlipping!!!\n")

#initializing var
head=0
tail=0

for flips in range(flip_number):
    #create the coin object
    coin = random.randint(0,1)

    if coin == 1:
        head += 1
        if choice.startswith("y"):
            print("HEADS")
    else:
        tail +=1
        if choice.startswith("y"):
            print("TAILS")

    if head==tail:
        print(f"At {flips+1} flips ,number of heads and tails were equal at {head} each")


head_perc = round(head*100/flip_number,2)
tail_perc = round(tail*100/flip_number,2)

#print the results
print(f"\nResults of flipping a coin {flip_number} times: ")
print("\nSide\t\tCount\t\tPercentage")
print(f"Heads\t\t{head}\t\t{head_perc}%")
print(f"Tails\t\t{tail}\t\t{tail_perc}")












