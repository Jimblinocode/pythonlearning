




tictactoe = [
            ["",  "",  "", ],
            ["",  "",  "", ],
            ["",  "",  "", ],
]





running = True

for item in tictactoe:
    print(item)

while running:
    # P1 input
    print("Player 1 (X) please enter 2 numbers, both between 0 and 2 for a row and a coulumn")
    num1 = int(input())
    num2 = int(input())
    if tictactoe[num1][num2] == "O":
        print("INVALID INPUT: Player 2 (O) has already chosen this spot")
    elif tictactoe[num1][num2] == "X":
        print("INVALID INPUT: you already chose this spot")
    else:
        tictactoe[num1][num2] += "X"
        for item in tictactoe:
            print(item)
    
    # horizontal win - P1

    if tictactoe[0][0] == "X" and tictactoe[0][1] == "X" and tictactoe[0][2] == "X":
        print("PLAYER 1 WINS")
        break
    elif tictactoe[1][0] == "X" and tictactoe[1][1] == "X" and tictactoe[1][2] == "X":
        print("PLAYER 1 WINS")
        break
    elif tictactoe[2][0] == "X" and tictactoe[2][1] == "X" and tictactoe[2][2] == "X":
        print("PLAYER 1 WINS")
        break

    # vertical win - P1
    if tictactoe[0][0] == "X" and tictactoe[1][0] == "X" and tictactoe[2][0] == "X":
        print("PLAYER 1 WINS")
        break
    elif tictactoe[0][1] == "X" and tictactoe[1][1] == "X" and tictactoe[2][1] == "X":
        print("PLAYER 1 WINS")
        break
    elif tictactoe[0][2] == "X" and tictactoe[1][2] == "X" and tictactoe[2][2] == "X":
        print("PLAYER 1 WINS")
        break
    
    # diagonal win - P1
    if tictactoe[0][0] == "X" and tictactoe[1][1] == "X" and tictactoe[2][2] == "X":
        print("PLAYER 1 WINS")
        break
    elif tictactoe[0][2] == "X" and tictactoe[1][1] == "X" and tictactoe[2][0] == "X":
        print("PLAYER 1 WINS")
        break




    # P2 input
    print("Player 2 (O) please enter 2 numbers, both between 0 and 2 for a row and a column ")
    num1 = int(input())
    num2 = int(input())
    if tictactoe[num1][num2] == "X":
        print("INVALID INPUT: Player 1 (X) has already chosen this spot")
    elif tictactoe[num1][num2] == "O":
        print("INVALID INPUT: you already chose this spot")
    else:
        tictactoe[num1][num2] += "O"
        for item in tictactoe:
            print(item)
    
    # horizontal win - P2

    if tictactoe[0][0] == "O" and tictactoe[0][1] == "O" and tictactoe[0][2] == "O":
        print("PLAYER 2 WINS")
        break
    elif tictactoe[1][0] == "O" and tictactoe[1][1] == "O" and tictactoe[1][2] == "O":
        print("PLAYER 2 WINS")
        break
    elif tictactoe[2][0] == "O" and tictactoe[2][1] == "O" and tictactoe[2][2] == "O":
        print("PLAYER 2 WINS")
        break
    
    # vertical win - P2

    if tictactoe[0][0] == "O" and tictactoe[1][0] == "O" and tictactoe[2][0] == "O":
        print("PLAYER 2 WINS")
        break
    elif tictactoe[0][1] == "O" and tictactoe[1][1] == "O" and tictactoe[2][1] == "O":
        print("PLAYER 2 WINS")
        break
    elif tictactoe[0][2] == "O" and tictactoe[1][2] == "O" and tictactoe[2][2] == "O":
        print("PLAYER 2 WINS")
        break
    
    # diagonal win - P2
    if tictactoe[0][0] == "O" and tictactoe[1][1] == "O" and tictactoe[2][2] == "O":
        print("PLAYER 2 WINS")
        break
    elif tictactoe[0][2] == "O" and tictactoe[1][1] == "O" and tictactoe[2][0] == "O":
        print("PLAYER 2 WINS")
        break
