
#We can use the return value of a function to show the outcome of the task like so:

def homework(math):
    answer = math * 10
    return answer

print(homework(10))

#This does the calculation of 10 and then prints the answer

#We can also use a variable to store this information:

def firstname(name):
    result = "My name is " + name
    return result

First_Name = firstname("Mary")
print(First_Name)    

#Note: If we do not include a return for a function it will show as none, you can check yourselve.