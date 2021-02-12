#Notes from Youtube - Python Tutorial (Mosh) from 1h22min on 2/11/2021

# i = 1
# while i <= 5:
#     print("*" * i)
#     i = i+1
# print('Done')

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count = guess_count + 1
#     if guess == secret_number:
#         print('You won!')
#         break
# else:
#     print('Better luck next time!')

# done_condition = False
# while done_condition == False:
#     command = input("What is your command? ").lower()
#     if command == 'help':
#         print('''Here are the game commands:
# help: shows this help screen
# start: starts the car
# stop: stops the car
# quit: quits this game''')
#     elif command == 'start':
#         print('Start your engines!  Your car has started.')
#     elif command == 'stop':
#         print('Screech!  Your car has stopped')
#     elif command == 'quit':
#         print('Thanks for playing!')
#         done_condition = True
#     else:
#         print("Command not understood. Try typing 'Help'")


# done_condition = False
# car_is_on = False
# while done_condition == False:
#     command = input("What is your command? ").lower()
#     if command == 'help':
#         print('''Here are the game commands:
# help: shows this help screen
# start: starts the car
# stop: stops the car
# quit: quits this game''')
#     elif command == 'start':
#         if car_is_on == False:
#             print('Start your engines!  Your car has started.')
#             car_is_on = True
#         else:
#             print('Car is already on!')
#     elif command == 'stop':
#         if car_is_on == False:
#             print('Car is already off!')
#         else:
#             print('Screech!  Your car has stopped')
#     elif command == 'quit':
#         print('Thanks for playing!')
#         done_condition = True
#     else:
#         print("Command not understood. Try typing 'Help'")

# for item in range(10):
#     print(item)

# prices = [10, 20, 30]
# total_price = 0
#
# for price in prices:
#     print(f"Item price is ${price}")
#     total_price += price
# print(f"Total price is ${total_price}")

# for x in range(4):
#     for y in range (4):
#         print(f"({x}, {y})")

letter_F = [5, 2, 5, 2, 2]
#
# for x in letter_F:
#     print('*' * int(x))

# output = ''
# for x in letter_F:
#     for y in range(x):
#         output += 'x'
#     print(output)
#     output = ''
# print('')
#
# letter_L = [2, 2, 2, 2, 5]
# #
# # for x in letter_F:
# #     print('*' * int(x))
#
# output = ''
# for x in letter_L:
#     for y in range(x):
#         output += 'x'
#     print(output)
#     output = ''

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# print(names)
# print(names[2])
# print(names[-1])
# print(names[1:3])
# print(names[3:2])
# names[0] = 'Jon'
# print(names[0])

# number = [2, 5, 12, 8, 6]
#
# largest_number = number[0]
# for x in number:
#     if x > largest_number:
#         largest_number = x
# print(largest_number)
#
# [
#     1 2 3
#     4 5 6
#     7 8 9
# ]
# 3x3
#
# 2-D list:
#
# matrix = [
#     [1, 2, 3],
#     [3, 4, 5],
#     [7, 8, 9]
# ]
#
# print(matrix[0][1])
# matrix[0][1] = 20
# print(matrix[0][1])
#
# for row in matrix:
#     for item in row:
#         print(item)

# numbers = [5, 2, 1, 7, 4]
# numbers.append(29)
# print(numbers)
# numbers.insert(0, 10)
# print(numbers)
# numbers.remove(5)
# print(numbers)
# numbers.pop()
# print(numbers)
# print(2 in numbers)
# numbers.append(10)
# print(numbers.count(10))
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
#
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers)
# print(numbers2)

numbers = [5, 2, 1, 7, 4, 4]

print(numbers)
current_value = numbers[0]
item_number = 0

for number in numbers:
    if current_value == number:
        numbers.remove(item_number)
        item_number += 1
print(numbers)