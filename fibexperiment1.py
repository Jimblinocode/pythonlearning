# an experiment to see what would happen if i iterated a recursive fibonnacci function and an incrementing variable through a while loop



def fib(n) -> int:
    if n == 1:
        return(0)
    elif n == 2:
        return(1)
    return fib(n - 1) + fib(n - 2)

running = True

num = 1

while running:
    print(num, fib(num))
    num += 1