#Looping through a list elements with a for loop

names=["pistu","oreo","hello","world"]

print(names)
print(type(names))

print(names[0].title())

for i in names:
    print(i.title())
    print("You r going to win this...\n")
print("Go football")

values=[1,2,3,4,5,9]
sum=0
for value in values:
    sum=sum+value
print(sum)

triples=[["a","b","c"],["1","2","3"],["do","re","me"]]
for triple in triples:
    print(triple)

for triple in triples:
    for element in triple:
        print(element,end=' ')


