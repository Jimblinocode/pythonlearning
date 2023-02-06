from random import randint

running = True

def fib(n) -> int:
    if n == 1:
        return(0)
    elif n == 2:
        return(1)
    return fib(n - 1) + fib(n - 2)

def magicfibball():
    num = randint(0,fib(20))
    num2 = fib(20)/4
    if num < num2:
        return("yeah huh")
    elif num == num2:
        return (num)
    elif num > num2:
        return ("nuh uh")

while running:
    com = input()
    print(magicfibball())


