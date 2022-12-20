# for loop practice

print("Please enter 10 numbers:")

numlist = []

for i in range(10):
    com = input()
    numlist.append(com)

larnum = 0
for item in numlist:
    if int(item) > larnum:
        larnum = int(item)
print("The largest number is " + str(larnum))
    
    
