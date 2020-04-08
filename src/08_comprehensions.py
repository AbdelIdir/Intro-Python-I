"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []
y = [data+1 for data in range(5)]
print(y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = []

y.append([num * num * num for num in range(10)])


print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [word.upper() for word in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?


# function that filters 
# def filterEven(data):

#     if(int(data) % 2 == 0):
#         return True
#     else:
#         return False


# filteredNumbers = filter(filterEven, x)
# print('The even numbers are:')
# y = [rightNumber for rightNumber in filteredNumbers]
# print(y)


y = [n for n in x if int(n) % 2 == 0]
