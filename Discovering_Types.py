
#There are 4 different types, int() bool() str() type(), 

#type(), checks if something is a bool, string, float or integer

is_on = True
number = 10
floatnumber = 12.5
name = "Bob"
print(type(is_on))
print(type(number))
print(type(floatnumber))
print(type(name))

#<class 'bool'>
#<class 'int'>
#<class 'float'>
#<class 'str'>

#int(), helps us convert data data types:

age = "16"
print(int(age))

#Turns a string into a integer

#int() removes the decimal point of a value

value = 9.99
print(int(value))

#int() on a boolean (1 \ 0) will be either True or False

#str() takes numerical values and convert them to strings to only be compared

password = 54987
str(password)
print(type(password))

#float() adds a deciaml point at the end of an value

years = 36
print(float(years))

#bool() Turns numbers, floats and strings into true or false

days = 26
months = 0
name = "Carter"
print(bool(days))
print(bool(months)) #This one will be false since it is 0, strings will be false if only ""
print(bool(name))
