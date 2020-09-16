users = ["pistu","oreo","hello","world"]

#Welcome msg
print("Welcome to the Shipping Account Program ")

#user input
name = input("\nWhat is your username: ").lower().strip()

#check gor users
if name in users:
    print(f"\nHello {name} ...Welcome back to your account")
    print("Current shipping prices are as follows:")

    print("\nShipping orders 0 to 100:   \t\t$5.10 each")
    print("Shipping orders 100 to 500:   \t\t$5.00 each")
    print("Shipping orders 500 to 1000:  \t\t$4.95 each")
    print("Shipping orders over 1000:    \t\t$4.80 each")
    nmbr = int(input("\nHow many items would you like to ship: "))
    if nmbr < 100:
        cost = 5.10
    elif nmbr < 500:
        cost = 5.00
    elif nmbr < 1000:
        cost = 4.95
    else:
        cost = 4.80
    bill = nmbr*cost
    bill = round(bill,2)
    print(f"To ship {nmbr} items it will cost you {bill} at {cost} per item ")
    decision = input("\nWould you like to place this orde (y/n): ").lower()
    if decision.startswith("y"):
        print(f"Okay. Shipping your {nmbr} items ")
    else:
        print("Okay. No order is placed")
else:
    print("Invalid username...")

