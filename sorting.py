#sorting list and len() fn

sports=["cricket","volleyball","golf","hockey"]
print(sports)
print(sorted(sports))
print(sorted(sports,reverse=True))
print(sports)
grades=[88,74,95,100,92]
print(sorted(grades))
print(sorted(grades,reverse=True))
print(grades)
length=len(grades)
print(length)
print(type(length))
removed_grade=grades.pop()
print(f"Removing grade {removed_grade}")
print(len(grades))
print(sports)
sports.sort()
print(sports)
grades.sort()
print(grades)
grades.sort(reverse=True)
print(grades)

print(sports)
sports.reverse()
print(sports)



