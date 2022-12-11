# running = True

# while running:
 #   com = input()
  #  if com == "exit":
  #      running = False

print("Please enter a command.")
print("Possible commands are...")

comlist = ["add", "subtract", "multiply", "divide", "exit/stop"]
running = True


for item in comlist:
    print(item)

while running:
    com = input()
    if com == "add":
        print("enter 2 numbers")
        num = input()
        num2 = input()
        ans = (int(num) + int(num2))
        print("the answer is " + str(ans))
    if com == "subtract":
        print("enter 2 numbers")
        num = input()
        num2 = input()
        ans = (int(num) - int(num2))
        print("the answer is " + str(ans))
    if com == "multiply":
        print("enter 2 numbers")
        num = input()
        num2 = input()
        ans = (int(num) * int(num2))
        print("the answer is " + str(ans))
    if com == "divide":
        print("enter 2 numbers")
        num = input()
        num2 = input()
        ans = (int(num) / int(num2))
        print("the answer is " + str(ans))
    if com == "exit" or "stop":
        running = False