import readchar
import os

POS_X = 0
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [10, 5]

map_objects = [[2, 3], [5, 4], [3, 4], [10, 6]]

while True:
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None

            for map_object in map_objects:
                if map_object[POS_Y] == coordinate_y and map_object[POS_X] == coordinate_x:
                    char_to_draw = "*"
                    object_in_cell = map_object

            if my_position[POS_Y] == coordinate_y and my_position[POS_X] == coordinate_x:
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                char_to_draw = "@"

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    #direction = input("¿Donde te quieres mover? [WASD]: ")
    direction = readchar.readchar()


    if direction == "w":
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "q":
        break

    # if my_position[POS_X] > 20:
    #     my_position[POS_X] = 0
    # elif my_position[POS_X] < 0:
    #     my_position[POS_X] = 20
    #
    #
    # if my_position[POS_Y] > 15:
    #     my_position[POS_Y] = 0
    # elif my_position[POS_Y] < 0:
    #     my_position[POS_Y] = 15

    os.system("clear")
