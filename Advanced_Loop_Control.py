
#We can use the Continue, Break and Else features to help our loops like so:

for x in range(7):
    x += 1
    if x == 4:
        continue
    print(x)

#We can use continue to skip a range number or variable

for y in range(12, 18):
    y += 1
    if y == 16:
        break
    print(y)

#We can use break to stop the loop from continuing, this one does not print 16 and above.

for z in range(30, 35):
    print(z)
else:
    print("Out of Numbers")

#Else will print if there is nothing left. 

#All of these variables if not defiened start on 0

#We can change the number and range for all of these statements with variables like for tasks in tasks.