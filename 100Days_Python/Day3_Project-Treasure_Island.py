# print("Welcome to the rollercoaster")
# height=int(input("What is your heigh in cm? "))
# bill = 0
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <=12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <=18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif 45 <= age <=55:
#         print("Everything is going to be ok. Have a free ride on us!.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#
#     wants_photo=input("Do you want to have a photo taken? Type y for Yes and n for No. ")
#     if wants_photo == "y" or wants_photo == "Y":
#         bill += 3 #Add $3 to their bill
#     print(f'Your final bill is {bill}')
# else:
#     print("Sorry you have to grow taller before you can ride.")

#########################################
# # Modulo Operator - getting the remainder of two number
# # Check Odd or Even
# number_to_check = int(input("What is the number you want to check? "))
# if number_to_check % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
#########################################
# weight = 85
# height = 1.85
#
# bmi = weight / (height ** 2)
#
# # 🚨 Do not modify the values above
# # Write your code below 👇
# if bmi <18.5:
#     print("underweight")
# elif bmi >= 18.5 and bmi <25:
#     print("normal weight")
# else:
#     print("overweight")
#########################################
# print("Welcome to Python Pizza Deliveries")
# small_pizza=15
# medium_pizza=20
# large_pizza=25
# bill=0
# size = input("What size of pizza do you want? S, M, or L: ")
# if size == "S" or size == "s":
#     bill=small_pizza
#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
#     if pepperoni == "Y" or pepperoni == "y":
#         bill +=2
# if size == "M" or size == "m":
#     bill=medium_pizza
#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
#     if pepperoni == "Y" or pepperoni == "y":
#         bill += 3
# elif size == "L" or size == "l":
#     bill=large_pizza
#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
#     if pepperoni == "Y" or pepperoni == "y":
#         bill += 3
# else:
#     print("You typed the wrong inputs.")
# extra_chesse = input("Do you want extra cheese? Y or N: ")
# if extra_chesse == "Y" or extra_chesse == "y":
#     bill += 1
# print(f'Your total bill is: P{bill}')

#########################################
#Day 3 Project: Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')
print("Welcome to Treasure Island. \nYour mission is to find the treasure.")
road_cross=input("You are at a cross road. Where do you want to go? \n     Type \"left\" or \"right\"\n").lower()
if road_cross == 'left':
    lake_cross=input("You've come to a lake. There is an island in the middle of the lake.\n     Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if lake_cross == "wait" or lake_cross == "Wait":
        door_color = input("You arrive at the island unharmed. There is house with 3 doors.\n     One red, one yellow, and one blue. Which color do you choose?\n").lower()
        if door_color == "red" or door_color == "blue":
            print("The room is full of pirates. You got killed. Game over!")
        elif door_color == 'yellow':
            print("You win!")
        else:
            print("You typed wrong. Game Over!")
    elif lake_cross == "swim":
        print("You got eaten by a shark. Game over!")
    else:
        print("You typed wrong. Game Over!")
elif road_cross == 'right':
    print("You fell in to a hole. Game over!")
else:
    print("You typed wrong. Game Over!")