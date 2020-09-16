#looping through a numerical range

#range() takes 2 parameters , start and the end , by default stepsize is one
values=range(1,10)
print(values)
print(type(values))

for i in range(1,10): #Values will stop at 10 ie on 9
    print(i)

#start will be by default 0 if not mentioned
for num  in range(5):
    print(num)

#third is an optional argumemnt for step size
for i in range(2,11,2):
    print(i)

word="Hello World"
list_word=list(word) #every element of the string will be stored in list as a single element
print(word)
print(list_word)

list_word[5]="New"
print(list_word)

#turning back to join strings
new_word="".join(list_word)
print(new_word)

nos=list(range(10,101,10))
print(nos)

for no in nos:
    print(no)

squares=[]
for no in nos:
    square=no**2
    squares.append(square)

print("Squares are:")
for square in squares:
    print(square)

cubes=[no**3 for no in nos]
for cube in cubes:
    print(cube)

print(min(cubes))
print(max(cubes))
print(sum(cubes))




