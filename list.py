#introduction to list
topics= ["physics","maths","chemistry"]
print(topics)
print(type(topics))

#print 1st element
print(topics[0])
print(topics[2])
print(type(topics[2]))

#print last element using -1, second last by -2
print(topics[-1])
colors=["red","blue","green"]
print(colors)
print(colors[2])

#changing value  of element of list
colors[2]="yellow"
print(colors)

#build dynamically list by default adds at the end of the list we can create new list 
colors.append("black")
print(colors)

#insert used to inser at specified index
colors.insert(1,"brown")
print(colors)


#for removing elemnts we use remove, it removes only one instance
colors.remove("red")
print(colors)

#stores and pop lassst element
removed=colors.pop()
print(removed)
removed1=colors.pop(1)
print(removed1)
print(colors)app
del colors[0]
print(colors)

fruit=[]
fruit.append(input("Enter a fruit"))
fruit.append(input("Enter a fruit"))
print(fruit)


















