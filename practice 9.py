# menu with for loop operations

# first basic phase, just asks you to input a number
print("Please enter a positive integer:")

com = input()

# second basic phase begins, asks you to enter a series of humbers based on the number you entered earlier
print("Please enter " + str(com) + " values")

# defining variables
intlist = []
oplist = ["1. Largest Value", "2. Smallest Value", "3. Does the value exist?", "4. Sum the list"]
running = True

# second phase process, appends every number you input in the second phase to the previously defined "intlist" variable. the amount of numbers you input in this process is the same amount as the number you input in the first phase. 
for i in range(int(com)):
    com2 = input()
    intlist.append(int(com2))

# Menu Begins
while running:
    print("Choose one of the following options:")
    for item in oplist:
        print(item)
    com = input()

    # First option process/output
    if com == "1":
        larnum = 0
        for item in intlist:
            if item > larnum:
                larnum = item
        print("the largest integer is " + str(larnum))
    
    # Second option process/output
    elif com == "2":
        larnum = 0
        for item in intlist:
            if item > larnum:
                larnum = item
        snum = larnum #intlist[0]
        for item in intlist:
            if item < snum:
                snum = item
        print("the smallest integer is " + str(snum))
    
    
    # Fourth option process/output
    elif com == "4":
        sum = 0
        for item in intlist:
            sum += item
        print("the sum of every integer is " + str(sum))
    
    # Exit command
    elif com == "exit":
        running = False
