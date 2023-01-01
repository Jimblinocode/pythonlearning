# Fibbonacci sequence challenge 

# driver code

print("What is the size of your fibbonacci sequence?")

com = input()

def Fibbonacci(size):
    fiblist = [0, 1]
    if size == 1:
        return[0]
    elif size == 2:
        return[0, 1]
    for item in range(2,size):
        fiblist.append(fiblist[item - 1] + fiblist[item - 2])  
    return(fiblist)

print("heres your fibbonacci sequence.")

print(Fibbonacci(int(com)))