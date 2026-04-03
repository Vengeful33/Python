
#We can use pop(), insert(), and append to change our lists

date = [12, 24]
date.append(36)
print(date)

#We can use append to add a date at the end

score = [78, 69, 24]
score.insert(0,43)
print(score)

#With insert we can chose where to add a value, this example is 0 at the beginning of the string

#For both insert and append, we can only add one element at a time

block = ["right", "left", "middle"]
block.pop()
print(block)

#pop removes the last value in a list, or by adding a index in the list we can remove a certian value