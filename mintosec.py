
com = int(input())

def mintosec(min):
    sec = min * 60
    return(sec)

def hourtosec(Hour):
    sec = Hour * mintosec(60)
    return(sec)

def daytosec(day):
    sec = day * hourtosec(24)
    return(sec)

def anytosec (any):
    pass

print(daytosec(com))


