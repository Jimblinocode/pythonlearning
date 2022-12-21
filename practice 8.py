# Totaling for loops

# Variables
oplist = ["1. sum", "2. product"]
oplist2 = []
running = True

# Defining input
print("enter 10 numbers:")
for i in range(10):
    com = input()
    oplist2.append(int(com))


# Menu
while running:
    print("Please choose which solution you would like:")
    for item in oplist:
        print(item)
    com = input()
# Processing/output
    if com == "1":
        sum = 0
        for item in oplist2:
            sum += item
        print("the sum of the numbers provided is " + str(sum))

    elif com == "2":
        sum = 1
        for item in oplist2:
            sum *= item
        print("the product of the numbers provided is " + str(sum))

    elif com == "exit":
        running = False