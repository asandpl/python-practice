# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
#
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

from random import randint

def find_common_elements(first_list, second_list):

    print(first_list)
    print(second_list)

    common_list = []

    for i in first_list:
        if i in second_list:
            if i not in common_list:
                common_list.append(i)


    # for i in first_list:
    #     duplicate = False
    #
    #     for c in common_list:
    #         if i == c:
    #             duplicate = True
    #             break
    #
    #     if not duplicate:
    #         for j in second_list:
    #             if i == j:
    #                 common_list.append(i)
    #                 break

    common_list.sort()
    print(common_list)


def generate_list():
    length = randint(10, 30)
    list = []
    i = 0

    while i < length:
        list.append(randint(1, 30))
        i+=1

    return list


first_list = generate_list()
second_list = generate_list()
find_common_elements(first_list, second_list)

