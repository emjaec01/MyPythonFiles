import random

#For loop
# fruits=['Apple','Peach','Pear']
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

########################################
# student_scores=[150, 23, 10, 100, 140, 105, 60, 87]
# # total_exam_score=sum(student_scores)   #OPTION 1
# # print(total_exam_score)
# #
# # #OPTION 2
# # sum_of_scores=0
# # for score in student_scores:
# #     sum_of_scores +=score
# # print(sum_of_scores)
#
# max_score=max(student_scores)    #OPTION 1
# print(max_score)
#
# #OPTION 2
# maximum_score=0
# for score_max in student_scores:
#     if score_max > maximum_score:
#         maximum_score = score_max
# print(maximum_score)

########################################
#Range function with For Loop
#RANGE- this function has to be used in conjunction with another function
# a=1
# b=6
# steps_size=1
#
# for number in range(a,b, steps_size): #count starts with 0
#     print(number)
#
# total=0
# for number in range(1,101):
#     total += number
# print(total)

########################################
# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

########################################
#Day 5 Project: Create a Password Generator
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
special_characters=['!','#','$','%','(',')','*','+']

print("Welcome to the PyPassword Generator!")
num_letters=int(input("How many letters would you like in your password?\n"))
num_symbols=int(input("How many symbols would you like?\n"))
num_numbers=int(input("How many numbers would you like?\n"))

#Easy Level
# password=""
#
# for char in range(0, num_letters):
#     password += random.choice(letters)
#     # print(password)
#
# for char in range(0, num_symbols):
#     password += random.choice(special_characters)
#     # print(password)
#
# for char in range(0, num_numbers):
#     password += random.choice(numbers)
#
# print(password)

#Hard Level
password_list=[]

for char in range(0, num_letters):
    password_list.append(random.choice(letters))
    # print(password)

for char in range(0, num_symbols):
    password_list.append(random.choice(special_characters))
    # print(password)

for char in range(0, num_numbers):
    password_list.append(random.choice(numbers))

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password=""
for char in password_list:
    password += char
print("*"*50)
print(f'Your password is: {password}')
print("*"*50)

