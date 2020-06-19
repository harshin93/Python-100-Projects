# Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.

import math
# pre define the value of width and height of the room

width_room = 15
print("The Width of the Room is {}".format(width_room))
height_room = 13
print("The Height of the Room is {}".format(height_room))

# calculating the cost

cost_of_width = int(input("Enter the cost for width: "))
cost_of_height = int(input("Enter the cost for height: "))
cost_of_tiles = (cost_of_width * 5) * (cost_of_height * 3)
print("Final cost of tiles is {}".format(cost_of_tiles))
