grid = [
    [" ", " ",  " "],
    [" ", " ",  " "],
    [" ", " ",  " "]
]

running = True

def gridprint(grid):
    for row in grid:
        for column in row:
            print(column, end=" ")
        print("\n", end="")

gridprint(grid)



while running:
    num = int(input())
    num2 = int(input())
    
    if grid[num][num2] == "X":
        print("bad")
    elif grid[num][num2] == "O":
        print("bad")
    else:
        grid[num][num2] = "X"
        gridprint(grid)

    num = int(input())
    num2 = int(input())

    if grid[num][num2] == "O":
        print("bad")
    elif grid[num][num2] == "X":
        print("bad")
    else:
        grid[num][num2] = "O"
        gridprint(grid)