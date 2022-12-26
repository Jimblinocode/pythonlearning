# function: all about input and output with side effects

# funtion example:
# var = 0

# function definition

# def add_two(num):
    # print("num is " + str(num))
    # return (num + 2)

# calling our function
# print("answer is " + str(add_two(var))) # => 6 + 2 => 8

# input: string
# no output
# side effect of putting the string on the terminal
# def print(string):
    # pass
    # put string on the terminal

# input()
# no inputs
# side effect: allows user to type on terminal, pauses the program (until input is received)
# output: evaluates to a string that contains whatever was entered in the terminal
# def input():
    # return # whatever was entered on the terminal


# scope: where can i use variables/functions
# global scope and local scope
# global scope: python file's scope
# local scope: scope relative to function
 
def greatest(list):
    var = list[0]
    for item in list:
        if item > var:
            var = item
    return (var)

peelist = [1, 2, 3, 4, 5, 6, 1, 39 ]

print( "the greatest number is " + str(greatest(peelist)))

var = 0
def func():
    global var
    var = 9
    print(var)

func()
print(var)