
#We have already establised that lists can be loacl or global scopes

def calculate_number(number):
    number = print(len(list1) == 3)
    return number

list1 = [11, 77, 83]

calculate_number(list1)

#We can also update are parameters like so

def find_game(game):
    print("Your favorite game is?")
    print(game)

game_list = ["COD", "Fallout", "Skyrim"]
find_game(game_list)

#This will put game list in the value of game.

#We can also use our function to receive certain elements from a list

def find_best_date(name):
    best_date = name[1]
    print(f"The best date you have been on is with {best_date}")

name = ["Sarah", "Carly", "Abigal"]
find_best_date(name)

#This will print Carly, we can also use name[1] as a variable and have it return

#We are also able to use while and for loops in funcions as well.