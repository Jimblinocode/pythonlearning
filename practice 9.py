# menu with for loop operations

print("Please enter a positive integer:")

com = input()

print("Please enter " + str(com) + " values")

intlist = []
oplist = ["1. Largest Value", "2. Smallest Value", "3. Does the value exist?", "4. Sum the list"]
running = True

for i in range(int(com)):
    com2 = input()
    intlist.append(int(com2))

while running:
    print("Choose one of the following options:")
    for item in oplist:
        print(item)
    com = input()

    if com == "1":
        larnum = 0
        for item in intlist:
            if item > larnum:
                larnum = item
        print("the largest integer is " + str(larnum))
    # elif com == "2":
        # smallnum = 0
        # for item in intlist:
            # if item < smallnum:
                # smallnum = item
    
    # putting a pin in this for now

    elif com == "4":
        sum = 0
        for item in intlist:
            sum += item
        print("the sum of every integer is " + str(sum))
