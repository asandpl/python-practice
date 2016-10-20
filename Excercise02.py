# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.


def odd_or_even():
    number = int(input("Please provice a number"))

    if (number % 2) == 1:
        print("Number", number, "is odd")
    else:
        print("Number", number, "is even")

