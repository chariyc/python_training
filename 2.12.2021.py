# 2.12.2021 -

# numbers = [4, 5, 5, 2, 1, 7, 4, 4, 4, 4]
# numbers2 = numbers.copy()
#
# print(f"This is numbers: {numbers}")
# print(f"This is numbers2: {numbers2}")
# count = 0
#
# for number in numbers:
#     print(f"Checking {number}")
#     for number2 in numbers2:
#         print(f"{number} = {number2}?")
#         if number == number2:
#             count += 1
#         if count > 1:
#             print(f"There is a duplicate of number: {number}")
#             print(f"Removing the duplicate now...")
#             numbers.remove(number)
#             print(f"{numbers} {count}x {number}")
#     count = 0
#     print(numbers)

# for number in numbers:
#     if current_value == number:
#         numbers.remove(item_number)
#         item_number += 1

#
# numbers = [4, 5, 5, 2, 1, 7, 4, 4, 4, 4]
# uniques = []
#
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# numbers = (1, 2, 3)
# numbers[0] = 10
# print(numbers[0])


# ## UNPACKING TUPLES AND LISTS
# coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
#
# x, y, z = coordinates
# print(f"{x} {y} {z}")


# ##DICTIONARIES
# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
#
# print(customer["name"])
# # print(customer["test"])
# # print(customer["Name"])
# customer["name"] = "Jack Smith"
# print(customer["name"])
#
# print(customer.get("birthdate", "Jan 1 1980"))

# number_to_text = {
#     "0": "Zero",
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine",
# }
#
# phone_number_in_text = ""
#
# phone_number = input("Phone: ")
#
# for number in phone_number:
#     phone_number_in_text += number_to_text.get(number, "None") + " "
#
# print(phone_number_in_text)

# message = input(">")
# words = message.split(' ')
# print(words)
#
# emojis = {
#     ":)": "😊",
#     ":(": "😒"
# }
#
# output = ""
#
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

# def greet_user():
#     print('Hi there!')
#     print('Welcome aboard!')
#
#
# print("Start")
# greet_user()
# print("finish")
# #
# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard!')
#
#
# print("Start")
# # greet_user(input("Name? "))
# greet_user("John", "Smith")
# greet_user(last_name="John", first_name="Smith")
# greet_user("John", last_name="Smith")
# print("finish")

## KEYWORD ARGUMENTS = USE FOR NUMERICALS
# calc_cost(total=50, shipping=5, discount=0.1)


# def square(number):
#     return number * number
#
#
# print(square(int(input("Number? "))))
#
# def square(number):
#     print(number * number)
#     return
#
#
# print(square(int(input("Number? "))))


# def emoji_convert(message):
#     emojis = {
#         ":)": "😊",
#         ":(": "😒"
#     }
#     words = message.split(' ')
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# print(emoji_convert(input("> ")))

# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(age)
# except ValueError:
#     print('Invalid value')
# except ZeroDivisionError:
#     print("Age can't be zero")


#class Point:
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()
#
# point2 = Point()
# point2.x = 1
# print(point2.x)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point(10, 20)
# print(point1.x)


# Person - name - talk()

# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def talk(self):
#         print(f"Hello {self.first_name} {self.last_name}")
#
#
# person1 = Person("Bob", "Dole")
# person1.talk()
#
# person2 = Person("John", "Smith")
# person2.talk()

## INHERITANCE
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def meow(self):
        print("meow")


dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 = Cat()
cat1.meow()