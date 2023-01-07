

# print("which do you want to do")

# comlist = ["1. minutes to seconds", "2. hours to seconds", "3. days to seconds"]

# for item in comlist:
    # print(item)


day = int(input())
hour = int(input())
minute = int(input())
second = int(input())

def mintosec(min):
    sec = min * 60
    return(sec)

def hourtosec(Hour):
    sec = Hour * mintosec(60)
    return(sec)

def daytosec(day):
    sec = day * hourtosec(24)
    return(sec)

def anytosec (day, hour, min, sec):
    sec = daytosec(day) + hourtosec(hour) + mintosec(min) + sec
    return(sec)

print(anytosec(day, hour, minute, second))

# if com == "1":
    # print("how many minutes?")
    # com2 = int(input())
    # print(mintosec(com2))

# elif com == "2":
    # print("how many hours?")
    # com2 = int(input())
    # print(hourtosec(com2))