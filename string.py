#strings

fullname="   Pistu oreo"
print(fullname)
print(fullname.upper())
print(fullname.lower())
print(fullname.title())

print(fullname.strip())
fullname=fullname.title().strip()
print(fullname)

fullname="\tPistu\noreo"
print(fullname)

first="pistu"
last="oreo"
fullname=first + " " + last
print(fullname.title())
print(first.upper() + " " + last.lower())
msg="Hello, how are you doing today? What is going at home?"
msg=msg.lower()
print(msg)

h_count=msg.count("h")
print(h_count)
print("Our msg has " + str(h_count) + " h")
#while concatenation data types should be same

lyric="Sometimes is seen a strange spot in the sky..."
lyric=lyric.lower()
s_count=lyric.count("s")
print(s_count)
print("Our lyric has", s_count, "s in it")
print("Our lyric has", s_count, "s in it", sep=" :-)")
#this is how you can use diff data types together


                    





