from os import system
# grid generation
grid = [["X" for i in range(3)]for i in range(3)]

def gridgen(grid):
    for row in grid:
        for item in row:
            print(item, end="")
        print("")
    return(grid)

title = [
    ["T", "I", "C"],
    ["A", " ", " "],
    ["C", " ", " "],
    ["T", "O", "E"]
]

def titleprint(title):
    for row in title:
        for item in row:
            print(item, end="")
        print("")
    return (title)


titleprint(title)
gridgen(grid)