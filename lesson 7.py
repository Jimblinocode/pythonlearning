# generators:
#   Generators are a quick way to generate lists
# ex: this creates a 3x3 grid
# newlist = [["" for _ in range(3)] for _ in range(3)]
# the first part prints 3 spaces in range of 0-2
# the second part then creates 3 rows of the previous generator that generated 3 spaces in a raneg of 0-2

# debugging in VScode:
    # you can choose the start point of your debugging process by clicking the red dot next to a line number
    # what VScodes debugger allows you to do is visualize memory and program flow in real time

# returning and unpacking tuples:
    # in a function you can return multiple values in a comma separated list
    # unpacking tuples is when you assign a tuples values to individual variables 
    # ex: x, y, z, = (0, 6, 9)
    # you take values out of the tuple and assign them to variables, thats why its called unpacking

# os module
# module that allows you to use terminal commands in code
# type "import os" and to use the system function type "os.system"

# . operator
# used before functions to indicate what module its from.
# used before methods to indicate the object its being called on.

# modulus operator %
# just finds the remainder of the division of 2 numbers
# modulo pattern:
    # 0%2 = 0
    # 1%2 = 1
    # 2%2 = 0
    # 3%2 = 1 
    # 4%2 = 0
    # (etc.)
    # same goes for x%3

# for x%y, as x increases from 0 onward, the result of the modulus operation will rotate from 0 - (y-1) 

# types of errors: 
# bugs: something doesn't do what you want it to do, but the code works
# exceptions: code crashes 
# ex: recursion limit reached, wrong opperand types
# try-except block is used to deal with exceptions. basically allows your code to run despite exceptions
# try:
    # code
# except:
    # code