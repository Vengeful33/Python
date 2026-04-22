
#We can use if, else and elif in functions like so:

def get_function(function):
    if function > 100:
        print("Your function is greater then 100")
    elif function < 100:
        print("Your function is less than 100")
    else:
        print("Your function is equal too 100")

get_function(101)
get_function(99)
get_function(100)