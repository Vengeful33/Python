#Anything after a # will be considered a comment

#This is going over the first section of Mimo's learning python

# If statement + Boolean (By Default True is True and False will be skipped):
if True:
    print ("Hello World")
#Code Block (2 Lines) with a Print Statement ("..."):

#This statement is skipped because it is false:
if False:
    print ("Hello World")

#Now we Implement a Variable:
Turned_On = True
if Turned_On:
    print ("On")

Turned_Off = False
if Turned_Off:
    print ("Off")

#This is in later sections, but a double negative makes a positive:
Turned_Off = False
if Turned_Off == False:
    print ("Off")

#The Answer should be:
#Hello World
#On
#Off