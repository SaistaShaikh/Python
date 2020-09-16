#string formatting methods

name="pistu"
age=20
money=9.3

#print using string concatenation
print(name + " is " + str(age) + " years old and has " + str(money) + " rs")

#print using .format() method for string
print("{0} is {1} and has ${2} dollars".format(name, age, money))

#print using f.strings
print(f"{name} is {age} and has {money} dollars")



