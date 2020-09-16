import datetime

#create the datetime obj and store the current date and time
time=datetime.datetime.now()
month=str(time.month)
day=str(time.day)
hour=str(time.hour)
minute=str(time.minute)

#welcome msg
print("Welcome to the grocery list app")
foods=["Meat","Cheese"]

print(f"Current date and time {month}/{day} \t{hour}:{minute}")
print(f"You currently have {foods[0]} and {foods[1]} in your list ")

#get user inpit
food=input("\nType of food to add to the grocery list:")
foods.append(food.title())
food=input("\nType of food to add to the grocery list:")
foods.append(food.title())
food=input("\nType of food to add to the grocery list:")
foods.append(food.title())

#print aand sort the list
print(f"Here is your grocery list\n{foods}")
foods.sort()
print(f"Here is your grocery list sorted\n{foods}")

#simulate shopping
print("\nSimulating grocery shopping")
print(f"\nCurrent grocery list {len(foods)} items")
print(foods)
buy_food=input("What food you buy just:").title()
foods.remove(buy_food)
print(f"Removing {buy_food} from the list...")
print(foods)
buy_food=input("What food you buy just:").title()
foods.remove(buy_food)
print(f"Removing {buy_food} from the list...")
print(foods)
buy_food=input("What food you buy just:").title()
foods.remove(buy_food)
print(f"Removing {buy_food} from the list...")
print(foods)

#The store is out of an item
print(f"\nCurrent grocery list: {len(foods)} items ")
print(foods)
no_item=foods.pop()
print(f"\nSorry, the store is out of {no_item}")

new_food=input("What food would you like instead:").title()
foods.insert(0,new_food)
print("\nHere is whats remains on your grocery list:")
print(foods)







