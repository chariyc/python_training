# 2.13.2021 - Python Youtube 2:11:55 forward
import random



# converters.py

# import converters
#
# print(converters.kg_to_lbs(70))


# from converters import kg_to_lbs
#
# print(kg_to_lbs(100))

# numbers = [10, 3, 6, 2]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)
#
def find_max(array):
    maximum = array[0]
    for number in array:
        if number > maximum:
            maximum = number
    return maximum

# print(find_max(numbers))
#
# # import utils
# #
# # numbers = [10, 3, 6, 2]
# # print(utils.find_max(numbers))
#
# # from utils import find_max
# #
# numbers = [10, 12, 3, 6, 2]
# # print(find_max(numbers))
#
# print(max(numbers))

# IMPORTING FUNCTIONS FROM A PACKAGE/MODULE
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()
#
# from ecommerce.shipping import calc_shipping
# calc_shipping()
