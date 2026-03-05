
#You can add to messages by adding string values in the code

print("New " + "Message")

#Should Print New Message

#You can also change out strings for variables

Number = "Ten"
print(Number + " Age")

#Prints 10 Age

#We can do the same for numbers

print("10 - 12")

#Prints 10 - 12, a number not in strings will display an error message

#In order to print numbers we need to do a f string (f"{}")

print(f"{10} New Messages")

#10 New Messages

#If a variable holds a number, put the variable in the F brackets, you can also add as many as you would like, you only need one f per line.

Age = 12
print(f"{Age} in {2025}")

#12 in 2025

#We can also use expresions like math in the {}

Number1 = 3000
Number2 = 2000
print(f"{Number1 - Number2} = True Number")

#1000 = True Number

#You can save a f string in a variable

today = 26
status = f"{today}"
print(status)

#26