numberOfStrings, fullTime, partTime = int(input("in_1: ")), 0, 0
for i in range(numberOfStrings):
    surnameNameAgeFullPartTime = input(f"in_{i + 2}: ")
    if surnameNameAgeFullPartTime[-4:] == "True":
        fullTime += 1
    else:
        partTime += 1
print(f"out: {fullTime}, {partTime}")
