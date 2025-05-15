#Pseudo Random Number Generator- Python uses Mersenne Twister
import random

# #Generating a number within the given range
# random_int=random.randint(0,1)
# print('Tossed a coin. Picked one \"heads\" or \"tails\"?')
# # print(random_int)
# if random_int == 0:
#     print('Heads.')
# elif random_int == 1:
#     print('Tails.')


#############################################
# #Generating a number from 0 to 1
# random_num_0_to_1=random.random()
# print(random_num_0_to_1)

#############################################
# #Generating a number float within the given range
# random_float=random.uniform(1,10)
# print(random_float)

#############################################
# #LISTS
# count_list=["one","two","three"]
# count_list[1]="twoH"  #modifying the content in the list
# print(count_list)
# count_list.append("four")   #appending a new entry to the end of the list
# print(count_list)
# count_list.extend(["five","six"])   #extending the list with new entries
# print(count_list)
# count_list.insert(2, "THREE")  #inserting an entry with a specific index in the lsit
# print(count_list)

#############################################
# #CHOOSE ONE RANDOMLY IN THE LIST?
# #OPTION 1
# NEMM=['Emjae','Jemmar','JC','JD','Gelo','Cliff']
# random_NEMM=random.choice(NEMM)
# print(random_NEMM)
#
# #OPTION 2
# random_index=random.randint(0,5)
# print(NEMM[random_index])

#############################################
# #More complex list
# fruits=['Strawberries','Nectarines', 'Apples', 'Grapes','Peaches','Cherries','Pears']
# vegetables=['Spinach','Kale','Tomatoes','Celery','Potatoes']
# dirty_frozen=[fruits, vegetables]
# print(dirty_frozen[1][1])

#############################################
#Day 4 Project: Rock Paper Scissors

player_choice=int(input("We are going to play rock, paper, scissors. \nWhat do you choose? \nType 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
art_rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

art_paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

art_scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices=['rock','paper','scissors']
game_images=[art_rock,art_paper,art_scissors]
comp_choice=random.randint(0,2)

# #OPTION 1
# if player_choice == 0 and comp_choice == 1:
#     print(f'Your choice is: {choices[0]}!\n{art_rock}\n')
#     print(f'Computer\'s choice is: {choices[1]}!\n{art_paper}\n')
#     print(f'You lose!')
# elif player_choice == 0 and comp_choice == 2:
#     print(f'Your choice is: {choices[0]}!\n{art_rock}\n')
#     print(f'Computer\'s choice is: {choices[2]}!\n{art_scissors}\n')
#     print(f'You win!')
# elif player_choice == 0 and comp_choice == 0:
#     print(f'Your choice is: {choices[0]}!\n{art_rock}\n')
#     print(f'Computer\'s choice is: {choices[0]}!\n{art_rock}\n')
#     print(f'It\'s a tie!')
# elif player_choice == 1 and comp_choice == 0:
#     print(f'Your choice is: {choices[1]}!\n{art_paper}\n')
#     print(f'Computer\'s choice is: {choices[0]}!\n{art_rock}\n')
#     print(f'You win!')
# elif player_choice == 1 and comp_choice == 2:
#     print(f'Your choice is: {choices[1]}!\n{art_paper}\n')
#     print(f'Computer\'s choice is: {choices[2]}!\n{art_scissors}\n')
#     print(f'You lose!')
# elif player_choice == 1 and comp_choice == 1:
#     print(f'Your choice is: {choices[1]}!\n{art_paper}\n')
#     print(f'Computer\'s choice is: {choices[1]}!\n{art_paper}\n')
#     print(f'It\'s a tie!')
# elif player_choice == 2 and comp_choice == 1:
#     print(f'Your choice is: {choices[2]}!\n{art_scissors}\n')
#     print(f'Computer\'s choice is: {choices[1]}!\n{art_paper}\n')
#     print(f'You win!')
# elif player_choice == 2 and comp_choice == 0:
#     print(f'Your choice is: {choices[2]}!\n{art_scissors}\n')
#     print(f'Computer\'s choice is: {choices[0]}!\n{art_rock}\n')
#     print(f'You lose!')
# elif player_choice == 2 and comp_choice == 2:
#     print(f'Your choice is: {choices[2]}!\n{art_scissors}\n')
#     print(f'Computer\'s choice is:2 {choices[2]}!\n{art_scissors}\n')
#     print(f'It\'s a tie!')
# else:
#     print(f'You typed an invalid number. You lose!')

#OPTION 2
if player_choice >=0 and player_choice <=2:
    print(f'You chose: {choices[player_choice]}')
    print(game_images[player_choice])

print(f'Computer chose: {choices[comp_choice]}')
print(game_images[comp_choice])
if player_choice >=3 or player_choice <0:
    print("You typed an invalid number. You lose!")
if player_choice == 0 and comp_choice == 2:
    print("You win!")
elif comp_choice == 0 and player_choice == 2:
    print("You lose!")
elif player_choice > comp_choice:
    print("You win!")
elif comp_choice > player_choice:
    print("You lose!")
elif comp_choice == player_choice:
    print("It\'s a tie!")
