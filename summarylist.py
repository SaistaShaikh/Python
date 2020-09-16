print("\t\tSummary Table")

num_strings=["100","15","55","42"]
print(f"\nThe variable num_string is a {type(num_strings)}")
print(f"It contains the elements: {num_strings}")
print(f"The element 15 is a {type(num_strings[0])}")

num_ints=[100,15,55,42]
print(f"\nThe variable num_ints is a {type(num_ints)}")
print(f"It contains the elements: {num_ints}")
print(f"The element 15 is a {type(num_ints[0])}")

num_floats=[2.2,5.0,1.25,0.2]
print(f"\nThe variable num_floats is a {type(num_floats)}")
print(f"It contains the elements {num_floats}")
print(f"The elements {num_floats[0]} is a {type(num_floats[0])}")


num_lists=[[1,2,3],[4,4,6],[7,8,9]]
print(f"\nThe variable num_lists is a {type(num_lists)}")
print(f"It contains the elements: {num_lists}")
print(f"The element {num_lists[0]} is a {type(num_lists[0])}")

#sorting
print("\nNow sorting num_strings and num_ints ")
num_strings.sort()
print(f"Sorted num_strigs: {num_strings}")
num_ints.sort()
print(f"Sorted num_ints: {num_ints}")
