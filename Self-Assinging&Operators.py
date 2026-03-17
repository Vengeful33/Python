
#We can update a variable using self-assignment, this sets a variable to its own value

money = 10
money = money
print(money)

#Prints 10

#We can change the variable like so:

sales = 12
sales = sales + 2
print(sales)

#Prints 14

name = "Ken"
name = name + " Robert"
print(name)

#Prints Ken Robert

#To make this process easier for numbers, we can use a += or a -= operator

date = 12
date += 6
print(date)

#Prints 18

time = 24
time -= 12
print(time)

#Prints 12