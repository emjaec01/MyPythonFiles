#Creating a function
def my_function():
    print("Hello")
    print("Bye")

#Calling the function
my_function()


########################################
#REEBORG'S  WORLD
#def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

########################################
#Day 6 Project:Escaping the Maze
#The secret is to have Reeborg follow along the right edge of the maze.
#SCENARIO 1: IF THERE IS ATLEAST 1 WALL IS PRESENT NEAR THE REEBORG
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

#SCENARIO 2: IF THERE IS NO WALL PRESENT AT FRONT AND RIGHT.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear() and right_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()