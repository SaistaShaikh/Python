#Welcome msg
print("Welcome to the Database Admin Program ")

#creating dictionary
Log_in_info = {
    "oreo":"Oreo#991",
    "pistu":"Pistu22222",
    "bob":"Bob55555555",
    "rehan":"24242488",
    "admin00":"88888888888"
}

#user input
user_name=input("\nEnter your username: ").lower()

if user_name in Log_in_info.keys():
    password=input("Enter your password: ")
    if password == Log_in_info[user_name]:
        print(f"Welcome {user_name}")
        if user_name=="admin00":
            for key,value in Log_in_info.items():
                print(f"Username: {key}\t Password: {value}")
        else:
            choice=input("Would you like to change your password? (y/n): ").lower()
            if choice=="y":
                new=input("Enter your new password...(min 8 character): ")
                if len(new)>=8:
                    Log_in_info[user_name]=new
                else:
                    
                    print("Not a validate password")

                print(f"Username: {user_name}\t Password: {Log_in_info[user_name]} ")
            else:
                print("Thank you Goodbye!")
    else:
        print("Incorrect Password!s")
else:
    print("Username not in DataBase ....Good bye!")

    




    
    
