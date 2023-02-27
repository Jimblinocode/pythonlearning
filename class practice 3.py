
import time

class profile:
    def __init__(self, name, dob, desc):
        self.name = name
        self.age = 2023 - dob
        self.desc = desc




print("What is your name")
namee = input()
print("When were you born?")
dob = int(input())
print("Write a description of yourself.")
desc = input()

you = profile(namee, dob, desc)

profdict = {
    "Name:      ": you.name,
    "Age:     ": you.age,
    "Description:       " : you.desc

}

for key in profdict:
    print("     ", key, profdict[key])








       