
#There are two different types of scopes local and global. 

#The main difference is that global can be accessed anywhere 

#While local is stored in a function.

def get_scope(scope):
    local_scope = scope
    print(local_scope)
    return local_scope

global_scope = "Global Scope"
print(global_scope)

#We can easily pring the global scope, but lets see if we try and print the local scope:

# print(local_scope) #

#Using the code above we get an error message, we have to print it this way

get_scope("Carl")

#We are able to get the local scope that way above

#Since global scopes are available we can make funcions like so

Number = 10

def find_true_number(Value):
    print(Number + Value)

find_true_number(55)

#This then prints 65
    