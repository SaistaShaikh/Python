colors=["red","blue","green"]
for color in colors:
    if color=="red":
        print(color.upper())
    else:
        print(f"Others {color}")
    

age = int(input("\nEnter your age: "))
if age< 18:
    print("You cannot gamble")
else:
    print("You can gamble")

list=[]
our_string=""
if our_string:
     print("Not empty")