def find_max(array):
    maximum = array[0]
    for number in array:
        if number > maximum:
            maximum = number
    return maximum