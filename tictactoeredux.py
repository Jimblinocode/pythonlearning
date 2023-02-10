from os import system
# grid generation
grid = [[" " for i in range(3)]for i in range(3)]

def gridgen(grid):
    for row in grid:
        for item in row:
            print(item, end="")
        print("")
    return(grid)




print("T I C T A C T O E")
gridgen(grid)

# Player controller
playernum = 0
player = ("X", "O", "@")

def gameplayloop():
    global playernum
    global player
    global cls
    while True:
        try:   
            print(f"Player {playernum + 1}, please enter 2 numbers between 0 and 2, the first one will represent a row, the second will represent the column ")
            n1, n2 = (int(input()), int(input()))
            if grid[n1][n2] == player[0] or grid[n1][n2] == player[1] or grid[n1][n2] == player[2]:
                print("SPOT TAKEN, PLEASE ENTER DIFFERENT COORDINATES")
            else:
                grid[n1][n2] = player[playernum]
                gridgen(grid)
                playernum += 1
                player[playernum] %= 2
                system(cls)

        except:
            print("INVALID CHARACTER, PLEASE ENTER A VALID NUMBER")
            n1, n2 = gameplayloop()


gameplayloop()