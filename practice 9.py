# menu with for loop operations

print("Please enter a positive integer:")

com = input()

print("Please enter " + str(com) + " values")

intlist = []
oplist = ["1. Largest Value", "2. Smallest Value" "3. Does the value exist? 4. Sum the list"]

for i in range(int(com)):
    com2 = input()
    intlist.append(com2)

