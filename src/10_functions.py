# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


num = input("Enter a number: ")
num = int(num)


def is_even(data):

    if(int(data) % 2 == 0):
        return True


# Read a number from the keyboard

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

if is_even(num):
    print("Even!")
else:
    print("Odd")
