# Take a list, say for example this one:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list th6at contains only elements from the original list a that are smaller than that number given by the user.

def list_less_than():
    number = int(input('Please provide a number:'))
    list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 4]
    new_list = []

    for i in list:
        if i < number:
            new_list.append(i)

    for i in new_list:
        print(i, end=' ')

