import random
print("Welcome to the Thesaurus App!" )

print("Choose a word from the thesasurus and I will give you a synonym ")

meaning = {
    'hot':['balmy','summery','tropical','boiling','scorching' ],
    'cold':['chilly','cool','freezing','frigad','polar'],
    'happy':['content','cheery','merry','jovial','jocular'],
    'sad':['unhappy','downcast','miserable','glum','melancholy']
}


print("Here are words in the thesauras")

for key in meaning.keys():
    print(f"\t-{key}")

word=input("\nWhat word would you like a synonym for:").lower()
 
if word in meaning.keys():
    index=random.randint(0,4)
    print(f"Synonym for {word} is {meaning[word][index]} " )
else:
    print("Sorry...that word is currently not in the thesaurus")

choice=input("\nWould you like to see the whole thesaurus (yes/no): ").lower()

if choice=="yes":
    for key,values in meaning.items():
        print(f"{key.title()} synonmys are: ")
        for value in values:
            print(f"\t{value}")


