# print("Hello World")
#
# age = 20
#
# first_name = "Mosh"
# age = 20
# is_online = False
#
# first = input("first: ")
# second = input("second: ")
#
# print(first + second)
# sum = float(first) + float(second)
# # print(int(first) + int(second))
# print("Sum: " + str(sum))

course = "Python for Beginners"

print(course.find("P"))
print(course.upper())
print(course.lower())
print(course.title())

print(course.replace('for', '4'))
print('Python' in course)

letters = []

for letter in course:
    if letter not in letters:
        letters.append(letter)

print(letters)

letters.sort()
print(letters)
print(len(numbers))

