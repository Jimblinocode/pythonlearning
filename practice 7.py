# for loop practice

print("Please enter 10 numbers:")

numlist = []

for i in range(10):
    com = input()
    numlist.append(int(com))

larnum = 0
for item in numlist:
    if item > larnum:
        larnum = item
print("The largest number is " + str(larnum))
    
    
