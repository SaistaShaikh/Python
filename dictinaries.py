fav_colors={
   'oreo':'black',
   'pistu':'red',
   'bob':'blue',
   'queen':'pink',
   'king':'red',
   'hello':'orange'

}

print(fav_colors)
fav_color_list=fav_colors.items()
print(fav_color_list)

for key,value in fav_colors.items():
   print(f"The key {key} has an associated value of {value}")

fav_color_keys=fav_colors.keys()
print(fav_color_keys)
for key in fav_colors.keys():
   print(f"{key.title()} thankyou for taking survey")

fav_color_values=fav_colors.values()
print(fav_color_values)

for value in set(fav_colors.values()):
   print(value)



user0={
   'name':'oreo',
   'age':'20'
}

user1={
   'name':'pistu',
   'age':'5'
}

user2={
   'name':'saista',
   'age':'10'
}

users=[user0,user1,user2]

for user in users:
   for key,value in user.items():
      print(f"{key.title()}: {value}")
   print("\n")

user=[]
for user in range(100):
   new_user={'name':'NA', 'age':0}
   users.append(new_user)

for user in users[:10]:
   print(user)














