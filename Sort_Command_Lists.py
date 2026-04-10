
#Just like .append(), .pop(), .insert(), we can use another command called .sort()

List1 = [11, 12, 6, 23]
List1.sort()

print(List1)

#The .sort() command will organize numbers from least to highest, if using negatives or floats they will still be oraganized like so

List2 = [-117, 7.77, 200, 0.12]
List2.sort()

print(List2)

#Note: You can not safe a sorted list in a variable, it prints none if doing so

List3 = [12, 1, 0]
NewList3 = List3.sort()

print(NewList3)

#We can also use strings for this command, it will organize it by Alphabetical Order

List4 = ["Sherry", "Zebra", "Alex"]
List4.sort()

print(List4)

#Using Booleans, puts false before True

List5 = [False, True, False]
List5.sort()

print(List5)