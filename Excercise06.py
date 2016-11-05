# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)


def reverse_string(str):
    i = len(str)
    rev = ""
    while i > 0:
        i -= 1
        rev += str[i]

    return rev


str = "qweewqa"
#rev = str[::-1]
rev = reverse_string(str)

print(str)
print(rev)

if str == rev:
    print(str + " is a palindrome")
else:
    print(str + " is not a palindrome")

