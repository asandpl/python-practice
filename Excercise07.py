# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even = [ i for i in list if i % 2 == 0]

# for i in list:
#     if i % 2 == 0:
#         even.append(i)

print(list)
print(even)

another = [ x*x for x in range(10)]
print(another)