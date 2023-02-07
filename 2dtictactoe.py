




tictactoe = [
            ["",  "",  "", ],
            ["",  "",  "", ],
            ["",  "",  "", ],
]





running = True

while running:
    print("Player 1 (X) please enter 2 numbers between 0 and 2 for a row and a coulumn")
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
    
    if tictactoe[0][0] == "X" and tictactoe[0][1] == "X" and tictactoe[0][2] == "X":
        print("PLAYER 1 WINS")
        break


    print("Player 2 (O) please enter 2 numbers between 0 and 2 for a row and a column ")
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
    
    if tictactoe[0][0] == "O" and tictactoe[0][1] == "O" and tictactoe[0][2] == "O":
        print("PLAYER 2 WINS")
        break
   


