import random
print("Welcome to the Rock Paper Scissors App")

rounds=int(input("\nHow many rounds would you like to play: "))

moves = ["rock","paper","scissors"]

p_score=0
c_score=0

for i in range(rounds):
    print(f"\nRound #{i+1}")
    print(f"Player: {p_score}\tComputer: {c_score}")

    c_index=random.randint(0,2)
    c_choice=moves[c_index]

    p_choice=input("Time to pick...rock paper scissor: ").lower().strip()

    if p_choice in moves:
            print(f"Computer: {c_choice}")
            print(f"Player: {p_choice}")

            if p_choice =="rock" and c_choice=="rock":
                winner="tie"
                phrase="It is a tie, how boring!"
            elif p_choice=="paper" and c_choice=="rock":
                winner="player"
                phrase="Paper covers rock"
            elif p_choice=="scissors" and c_choice=="rock":
                winner="computer"
                phrase="Rock smashes scissors"

            elif p_choice=="paper" and c_choice=="paper":
                winner="tie"
                phrase="It is a tie, how boring!"
            elif p_choice=="rock" and c_choice=="paper":
                winner="computer"
                phrase="Paper covers rock"
            elif p_choice=="scissors" and c_choice=="paper":
                winner="player"
                phrase="scissors cut paper"

            elif p_choice=="scissors" and c_choice=="scissors":
                winner="tie"
                phrase="It is a tie, how boring!"
            elif p_choice=="paper" and c_choice=="scissors":
                winner="computer"
                phrase="scissors cut paper"
            elif p_choice=="rock" and c_choice=="scissors":
                winner="computer"
                phrase="Rock smashes scissors"
            else:
                print("Round not calculated")
                winner="tie"
                phrase="It is a tie, how boring!"
            
            print(f"\t {phrase}")
            if winner=="player":
                print(f"\tYou win the round {i + 1}")
                p_score+=1
            elif winner=="computer":
                print(f"\tComputer win round {i+1}")
                c_score+=1
            else:
                print("\tThis round is a tie")
            
    else:
        print("That is not a valid game option:")
        print("Computer gets the score")
        c_score+=1


print("\nFinal game results")
print(f"\tRounds played: {i+1}")
print(f"\tPlayer score: {p_score}")
print(f"\tComputer score: {c_score}")
if p_score>c_score:
    print("\n\tWinner:  Player")
elif p_score<c_score:
    print("\n\tWinner:  Computer :(")
else:
    print("\tIt is tie")














