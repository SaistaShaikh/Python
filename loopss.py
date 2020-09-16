names=["oreo","pistu","hello","world"]
nos=[6,8,9,1]

for i in range(len(names)):
    print(f"{names[i].title()} : {nos[i]}")

#zip(), takes multiple parameters
for name, no in zip(names,nos):
    print(f"{name.title()} : {no}")