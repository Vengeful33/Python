
#We can creat a tuple to store multiple types of information:

class_tuples = (1979, "David", True)
print(class_tuples)

#In cases with only one value, we want to add a comma at the end:

new_tuple = ("New",)
print(new_tuple)

#We are able to save tuples in lists like so:

new_list = [(new_tuple), (class_tuples)]
print(new_list)

#Each tuple is able to be a value:

print(len(new_list))

#This Equals 2

#Or we can access a certain value by it's index"

print(new_list[1])

#We can also save them in a variable and use them in a for loop:

old_list = [("John", 1984),("Sierra", 1993)]

for value in old_list:
    print(f"Your data: {old_list}")