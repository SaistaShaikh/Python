#welcome msg
print("Welcome to the Binary/Hexadecimal Converter App")

#user input
max_value=int(input("\nCompute binary and Hexadecimal values up to following decimal number: "))
decimal=list(range(1,max_value+1))
binary=[]
hexadecimal=[]

#using bin() and hex()
for i in decimal:
    binary.append(bin(i))
    hexadecimal.append(hex(i))

print("\nGenerating lists...Complete!")

#for slicing taking user input
print("\nUsing slicing, we will now show a portion of each list.")
lower_range=int(input("What decimal no would you like to start at: "))
upper_range=int(input("What decimal no would you like to stop at: "))

print(f"Decimal values from {lower_range} to {upper_range}:" )
for i in decimal[lower_range-1:upper_range]:
    print(i)

print(f"Binary values from {lower_range} to {upper_range}:" )
for i in binary[lower_range-1:upper_range]:
    print(i)

print(f"Hexadecimal values from {lower_range} to {upper_range}:" )
for i in hexadecimal[lower_range-1:upper_range]:
    print(i)   

#print entire list
input(f"\nPress Enter to see all values from 1 to {max_value}")
print("Decimal\tBinary\tHexadecimal")
print("---------------------------------------------")
for d,b,h in zip(decimal, binary, hexadecimal):
    print(f"{d}\t{b}\t{h}")




