#Functions
'''
def my_function(something):   ##############with inputs
    #Do this with something
    #Then do this
    #Finally do this
'''
from isort.wrap_modes import backslash_grid
from selenium.webdriver.common.devtools.v85.fetch import continue_request

##########################################################
# def greet():
#     print("Hey!")
#     print("Good day!")
#     print("Have a nice day.")
#
# greet()

##########################################################
# def greet_with_name(name):
#     print(f'Hello, {name}')
#     print(f'Good day {name}!')
#     print(f'Have a nice day {name}!')
#
# greet_with_name("Emjae")

##########################################################
#Life in Weeks
# def life_in_weeks(current_age):
#     weeks_in_a_year=52.1786
#     years_left=90 - current_age
#     years_left_in_weeks=years_left*weeks_in_a_year
#     print(years_left_in_weeks)
# life_in_weeks(26)

##########################################################
#more than 1 parameter
# def greet_with(name, location):
#     print(f'Hi, {name}')
#     print(f'What it is like in {location}')
#
# greet_with("Emjae", "nowhere")

##########################################################
#LOVE CALCULATOR
# def calculate_love_score(name1, name2):
#     combined_names = name1 + name2
#     lower_names = combined_names.lower()
#
#     t = lower_names.count("t")
#     r = lower_names.count("r")
#     u = lower_names.count("u")
#     e = lower_names.count("e")
#     first_digit = t + r + u + e
#
#     l = lower_names.count("l")
#     o = lower_names.count("o")
#     v = lower_names.count("v")
#     e = lower_names.count("e")
#     second_digit = l + o + v + e
#
#     score = int(str(first_digit) + str(second_digit))
#     print(score)
#
#
# calculate_love_score("Kanye West", "Kim Kardashian")

##########################################################
from cipher_art import cipher_ascii
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(cipher_ascii)
# process_type=input(f'Type \'encode\' to encrypt, type \'decode\' to decrypt:\n').lower()
# text=input(f'Type your message:\n').lower()
# shift=int(input(f'Type the shift number:\n'))
#
# def encrypt(original_text, shift_amount):
#     cipher_text=""
#     for letter in original_text:
#         shifted_position=letters.index(letter)  + shift_amount
#         shifted_position %= len(letters)
#         cipher_text += letters[shifted_position]
#     print(f'Here is the {process_type} result: {cipher_text}')
#
# def decrypt(original_text, shift_amount):
#     output_text = ""
#     for letter in original_text:
#         shifted_position = letters.index(letter) - shift_amount
#         shifted_position %= len(letters)
#         output_text += letters[shifted_position]
#     print(f'Here is the {process_type} result: {output_text}')
#
# def caesar(original_text, shift_amount, direction):
#     output_text = ""
#     for letter in original_text:
#         if direction == 'decode':
#             shift_amount *= -1
#         shifted_position = letters.index(letter) + shift_amount
#         shifted_position %= len(letters)
#         output_text += letters[shifted_position]
#     print(f'Here is the {process_type} result: {output_text}')


def caesar_x(original_text, shift_amount, direction):
    output_text=""
    if direction == 'decode':
        shift_amount *= -1
    for letter in original_text:
        if letter not in letters:
            output_text += letter
            # print(output_text)
        else:
            shifted_position = letters.index(letter) + shift_amount
            shifted_position %= len(letters)
            output_text += letters[shifted_position]
    print(f'Here is the {process_type} result: {output_text}')

should_continue=True
while should_continue:
    process_type = input(f'Type \'encode\' to encrypt, type \'decode\' to decrypt:\n').lower()
    text = input(f'Type your message:\n').lower()
    shift = int(input(f'Type the shift number:\n'))

    caesar_x(text, shift, process_type)

    ask_for_another_try = input(f'Type \'yes\' if you want to go again. Otherwise type \'no\'.').lower()
    if ask_for_another_try == "no":
        should_continue=False
        print(f'Goodbye')









