print("Welcome to the Basketball Roster Program ")


roster=[]

#user input
player=input("\nWho is your point guard:").title()
roster.append(player)
player=input("Who is your shooting guard:").title()
roster.append(player)
player=input("Who is your small forward:").title()
roster.append(player)
player=input("Who is your power forward:").title()
roster.append(player)
player=input("Who is your center:").title()
roster.append(player)

#display roster
print("\n\tYour starting 5 for the upcoming basketball season")
print(f"\t\tPoint Guard\t\t{roster[0]}")
print(f"\t\tShooting Guard\t\t{roster[1]}")
print(f"\t\tSmall Forward\t\t{roster[2]}")
print(f"\t\tPower Forward\t\t{roster[3]}")
print(f"\t\tCenter\t\t\t{roster[4]}")

#remove an injured player
injured_player=roster.pop(2)
print(f"\nOh no! {injured_player} is injured")

roster_length=len(roster)
print(f"Your roster only has {roster_length} players")

#add a new player
added_player=input(f"Who will take {injured_player}'s spot:").title()
roster.insert(2,added_player)

#Display roster
print("\n\tYour starting 5 for the upcoming basketball season")
print(f"\t\tPoint Guard\t\t{roster[0]}")
print(f"\t\tShooting Guard\t\t{roster[1]}")
print(f"\t\tSmall Forward\t\t{roster[2]}")
print(f"\t\tPower Forward\t\t{roster[3]}")
print(f"\t\tCenter\t\t\t{roster[4]}")

print(f"\nGood Luck {roster[2]} you will do great!")
roster_length=len(roster)
print(f"\nYour roster now have {roster_length} players")




