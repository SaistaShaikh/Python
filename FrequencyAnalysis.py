from collections import Counter

# Welcome message
print("Welcome to the Frequency Analysis App")

#non-letter list
non_letter=['!', '@', '#', '$', '%', '^', '&', '*', ' ', '.', '/', ':' ,'?', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '\n', '\t', ',' '(', ')', '"', "'"]

#get user input
key_phrase_1=input("\nEnter a word or phrase to count occurence of each letter: ").lower().strip()

#removing non-letter
for i in non_letter:
    key_phrase_1=key_phrase_1.replace(i,'')

#length after removing non-letters
total=len(key_phrase_1)

#create a counter obj
letter_count=Counter(key_phrase_1)

print("\nHere  is the frequency analysis from key phrase 1: ")
print("\n\tLetter\t\tOccurence\tPercentage")

#determine freq analysis 
for key,value in sorted(letter_count.items()):
    perc=100*value/total
    perc=round(perc,2)
    print(f"\t{key}\t\t{value}\t\t{perc}%")

order=letter_count.most_common()
ordered=[]

for i in order:
    ordered.append(i[0])

print("\nLetters ordered from highest occurence to lowest: ")
for i in ordered:
    print(i,end='')

