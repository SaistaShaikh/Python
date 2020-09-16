#Welcome
print("Welcome to the Fibonacci Calculator App ")

#user input
no=int(input("How many digits of the Fibonacci Sequence would you like to compute: "))

#compute the value of the fib
fib=[1,1]

for i in range(no-2):
    new_fib=fib[i] + fib[i+1]
    fib.append(new_fib)
#Displaying values
print(f"\nThe first {no} numbers of fibonacci series are: ")
for i in fib:
    print(i)

#compute the golden ratio
golden=[]
for i in range(len(fib)-1):
    ratio=fib[i+1]/fib[i]
    golden.append(ratio)
print(f"\nThe corresponding golden values are: ")
for i in golden:
    print(i)