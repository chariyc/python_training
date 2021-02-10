# # 2.10.2021 - https://www.youtube.com/watch?v=_uQrJ0TkZlc&ab_channel=ProgrammingwithMosh
# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# print("Mosh")
# print('o---- ' * 3)
# print(' |||| ' * 3)
# print('*' * 10)
#
# price = 10.1
# print('price = ' + str(price))
#
# name = 'Mosh'
# is_published = False
#
# patient_name = input('What is the patient name? ')
# # patient_name = 'John Smith'
# age = input('What is the patients age ? ')
# #age = 20
# is_new_patient = input('Is this a new patient? (Y/N) ')
#
# if is_new_patient == 'Y':
#     statement = 'a new patient'
# else:
#     statement = 'not a new patient'
#
# print(patient_name + ' is ' + str(age) + ' and is ' + statement)
#
# name = input('What is your name? ')
# favorite_color = input('What is your favorite color? ')
# print('Nice to meet you ' + name + '. My favorite color is ' + favorite_color + ' too!')
#
# birth_year = input('What year were you born? ')
# age = 2021 - int(birth_year)
# print('You are ' + str(age) + ' years old.')
#
# weight_in_pounds = input('How much do you weigh (in pounds)? ')
# weight_in_kg = int(weight_in_pounds)/2.2
# print('You weigh ' + str(weight_in_kg) + 'kg.')
#
# number = input('What is your number? ')
# sig_dig = input('How many significant digits do you want? ')
# print('Your number is rounded to: ' + str(round(float(number),int(sig_dig))))
#
# weight_in_pounds = input('How much do you weigh (in pounds)? ')
# weight_in_kg = int(weight_in_pounds)/2.2
# print('You weigh ' + str(round(float(weight_in_kg),2)) + 'kg.')
#
# from math import log10, floor
# def round_to_1(x):
#     return round(x, -int(floor(log10(abs(x)))))
#
# print(round_to_1(0.0232))
# print(round_to_1(1234243))
# print(round_to_1(13))
# print(round_to_1(4))
# print(round_to_1(19))
#
# # rounding to the largest significant digit
# from math import log10, floor
# def round_to_1(x):
#     return round(x, -int(floor(log10(abs(x)))))
# print(round_to_1(3.1415))
# print(round_to_1(5351))
# print(round_to_1(17))
#
# print("Python's course for Beginners")
# print('Python course for "Beginners"')
# print('''
# Hi John,
#
# Here is the first course for you.
# example of " and '
#
# Sincerely,
# Charles''')
#
# course = 'Python for Beginners'
# print(course[1])
# print(course[-1])
# print(course[0])
# print(course[0:3]) #excluding the last index
# print(course[0:25])
# print(course[0:])
# print(course[:])
# print(course[-5:])
#
# another_course = course[:]
# print(another_course)
#
# name = 'Jennifer'
# print(name[1:-1])
#
# first_name = 'John'
# last_name = 'Smith'
# message = first_name + ' ' + last_name + ' is a coder.'
# print(message)
#
# msg = f'{first_name} [{last_name}] is a coder.'  #formatted string
# print(msg)
#
# course = 'Python for Beginners'
# print(course.upper())
# print(course)
# print(course.lower())
#
# print(course.find('P'))
# print(course.find('O'))
# print(course.find('Beg'))
#
# print(course.replace('Beginners','Absolute Beginners'))
#
# print(course.replace('n','m'))
#
# print('Python' in course)
# print('python' in course)
#
# print(len(course))
# print(course.title())
#
# print(10 * 3)
# print(10 ** 3)
#
# x = 10
# x -= 3
# print(x)
#
# x=10
# x += 3
# print (x)
#
# x = 10 + 3 * 2
# print(x)
#
# # precidence: exponentiation, mult/division, addition/subtraction
#
# x = (2 + 3) * 10 - 3 ** 3
# print(x)
#
# import math
#
# x = 2.9
# print(math.ceil(2.9))
# print(math.floor(2.9))
#
# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day.")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day.")
#     print("Dress warmly.")
# else:
#     print("It's a beautiful day.")
# print("Enjoy your day!")
#
# house_price = 1000000
# credit_good = True
#
# if credit_good:
#     down_payment = round((house_price / 10), 2)
# else:
#     down_payment = round((house_price / 5), 2)
#
# print("The downpayment is $" + str(down_payment))
# print(f"Down payment: ${down_payment}")
#
# has_high_income = True
# has_good_credit = True
#
# if has_high_income and has_good_credit:
#     print("eligible for loan")
#
# if has_high_income or has_good_credit:
#     print("might be eligible")
#
# has_criminal_record = True
#
# if has_good_credit and not has_criminal_record:
#     print("eligible for loan")
#
# name = input("What is your name? ")
#
# if len(name) < 3:
#     print("Your name is too short!")
# elif len(name) > 10:
#     print("Your name is so long!")
# else:
#     print(f"Hello {name}!")
#
# weight = float(input("What is your weight? "))
# kg_or_lbs = input("(K)g or (L)bs? ")
#
# if kg_or_lbs == "k" or kg_or_lbs == "K":  # kg_or_lbs.upper()
#     kg = True
#     weight_in_lbs = round((weight * 2.2),2)
#     print(f"Your weight is {weight_in_lbs} pounds.")
# elif kg_or_lbs == "l" or kg_or_lbs == "L":
#     lbs = True
#     weight_in_kgs = round((weight / 2.2),2)
#     print(f"Your weight is {weight_in_kgs} kilograms.")
#

