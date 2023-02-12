from os import system
# grid generation
grid = [[" " for i in range(3)]for i in range(3)]

def gridgen(grid):
    for row in grid:
        for item in row:
            print(item, end=" ")
        print("")
    return(grid)



#win/draw state 2
def diags(grid):
    newlist = []
    newlist.append([grid[i][i] for i in range(3)])
    newlist.append([grid[i][2-i]] for i in range(3))
    return(newlist)

def transpose(grid):
    newlist = [[None for coli in range(len(grid))] for rowi in range(len(grid))]
    for rowi in range(len(grid)):
        for coli in range(len(grid[rowi])):
            newlist[rowi][coli] = grid[coli][rowi]
    return (newlist)


# Player controller

playernum = 0
playerchar = ("X", "O")
running = True
def gameplayloop():
    global running
    global playernum
    global playerchar
    while running:
        try:
            print("T I C T A C T O E")
            gridgen(grid)
            playernum %= 2
            player = playerchar[playernum]
            playernum += 1
            print(f"Player {playernum}, please enter 2 numbers between 0 and 2, the first one will represent a row, the second will represent the column ")
            n1, n2 = (int(input()), int(input()))
            if grid[n1][n2] == playerchar[playernum - 1] or grid[n1][n2] == playerchar[playernum%2] or grid[n1][n2] == playerchar[playernum - 2]:
                print("SPOT TAKEN, PLEASE ENTER DIFFERENT COORDINATES")
            else:
                grid[n1][n2] = player
                system("cls")
                #win/draw state
            for row in grid:
                if row == [player, player, player]:
                    print("T I C T A C T O E")
                    gridgen(grid)
                    print(f"P{playernum} WINS!")
                    running = False
            for row in diags(grid):
                if row == [player, player, player]:
                    print("T I C T A C T O E")
                    gridgen(grid)
                    print(f"P{playernum} WINS!")
                    running = False
            for row in transpose(grid):
                if row == [player, player, player]:
                    print("T I C T A C T O E")
                    gridgen(grid)
                    print(f"P{playernum} WINS!")
                    running = False
        except:
            print("INVALID INPUT")
            n1, n2 = gameplayloop()





gameplayloop()







