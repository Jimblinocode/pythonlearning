print("enter a number between 0 and 100")

num = input()
goal = 50
min = 0
max = 100

if int(num) < min or int(num) > max:
    print("invalid number, please try again")
elif int(num) > goal:
    print("Number entered is higher than 50, try again")
elif int(num) == goal:
    print("Bullseye")
else:
    print("Number entered is below 50, try again")

