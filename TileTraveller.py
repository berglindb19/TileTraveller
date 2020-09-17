# Algorithm
# For every tile that the user is located at any given time, the user is told in what direction he can travel.
# User chooses one of these directions, but if he chooses a direction that is not one of the option the program prints "Not a valid direction!"
# When the user enters the (3,1) tile he wins, it's the victory tile. 
# At the beginning of the game the variable named victory = False
# Also, at the beginning of the game we need to give beginning tile, which is (1,1)
# Throughout the game a loop runs while victory != False 
# Use if-sentences for every tile to tell the user in which dircetion he can travel
# When the user/player wins the game, at tile (3,1) the victory variable turns into True

def change_location_NS(direction):
    direction = direction.lower()
    if direction == 'n':
        return location_NS + 1
    if direction == 's':
        return location_NS -1
    else:
        return location_NS

def change_location_EW(direction):
    direction = direction.lower()
    if direction == 'e':
        return location_EW + 1
    if direction == 'w':
        return location_EW -1
    else:
        return location_EW

vicoty = False
location_NS = 1
location_EW = 1

while vicoty != True:
    valid_directions = direction_options(location_NS, location_EW)

    print('You can travel:', valid_directions)
    direction = input('Direction: ')

    if direction != valid_directions:
        print("Not a valid direction!")
    else:
        location_NS = change_location(direction)
        location_EW = change_location(direction)
    
    vicoty = is_victory(location_NS, location_EW)