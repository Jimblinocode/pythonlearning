import time
from os import system
# print(dir(time))

# print(time.altzone)



while True:
    lt = time.asctime(time.localtime())
    system("cls")
    print(lt)