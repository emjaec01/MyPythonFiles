# #Subscripting
# print("Hello"[0])
# #Data Types: String(Str), Integers(Int), Float(float), Boolean(bool)
# #Large integers
# print(123_456_789)
#################################
# print(type("abc"))
# print(type(123))
# print(type(3.14))
# print(type(True))
#################################
# #Converting data types
# print(int("123")+int("123"))
#################################
# #Fix this code: print("Number of letters in your name: " + len(input("Enter your name: ")))
# print("Number of letters in your name: " + str(len(input("Enter your name"))))
# #OR
# name_of_the_user=input("Enter your name")
# length_of_name=len(name_of_the_user)
# print("Number of letters in your name: " + str(length_of_name))
#################################
# #Implicitly typecasting - converting the result into float
# print(6/3)
# #You can use this code if you don't want float result
# print(6//3)
#################################
# # Calculate the BMI. flooring(rounding) the result to a whole number
# height= 1.65
# weight= 84
# bmi= weight / (height**2)
# print(round(bmi))
#################################
# #Assignment Operators: += , -= , *= , /=
# score = 0
# score += 1
# print(score)
#
# #using f-string and curly braces.
# score = 0
# height = 1.8
# is_winning = True
# print(f'Your score is = {score}, your height is {height}. You are winning is {is_winning}')
#################################
#Day 2 Project: Tip calculator
# # Using if function
# print('Welcome to the tip calculator!')
# food_bill=input(f'What was the total bill? P')
# bill_tip=input(f'How much tip would you like to give? 10, 12, or 15? ')
# total_people=input(f'How many people to split the bill? ')
# if bill_tip == "10":
#     total_billTip = float(food_bill) * 1.10
# elif bill_tip == "12":
#     total_billTip = float(food_bill) * 1.12
# else:
#     total_billTip = float(food_bill) * 1.15
# bill_perPerson = total_billTip / int(total_people)
# print(bill_perPerson)

print('Welcome to the tip calculator!')
food_bill=float(input(f'What was the total bill? P'))
bill_tip=int(input(f'How much tip would you like to give? 10, 12, or 15? '))
total_people=int(input(f'How many people to split the bill? '))
total_bill = food_bill + food_bill*(bill_tip / 100)
bill_perPerson = total_bill / total_people
final_amount= round(bill_perPerson, 2)
print(f'Each person should pay: P{final_amount}')
