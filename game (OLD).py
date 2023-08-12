import os

##Global variables
#If move is 
#0: not used
#1: X
#2: O
usedMoves = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
symbols = {
    0: ' ',
    1: 'X',
    2: 'O'
}

##Functions
#Print selection board
def selectionBoard():
    print("| 0 | 1 | 2 |")
    print("| 3 | 4 | 5 |")
    print("| 6 | 7 | 8 |")

#Print current board
def printBoard():
    for row in usedMoves:
        for value in row:
            if value in symbols:
                symbol = symbols[value]
            print("| " + symbol + "", end=' ')
        print("|")
    print()

#User selection
def userBoardSelection():
    while (True):
        try:
            userMove = int(input("X's turn. Input move (0-8): "))
            row = userMove // len(usedMoves[0])
            col = userMove % len(usedMoves[0])

            if 0 <= row < len(usedMoves) and 0 <= col < len(usedMoves[0]):
                if usedMoves[row][col] == 0:
                    print("X makes a move to square " + str(userMove))
                    usedMoves[row][col] = 1
                    printBoard()
                    break
                else:
                    print("Already taken.")
            else:
                print("Out of range!")

        except ValueError:
            print("Not a number!")

#Bot selection
def botBoardSelection():
    while (True):
        try:
            userMove = int(input("X's turn. Input move (0-8): "))
            row = userMove // len(usedMoves[0])
            col = userMove % len(usedMoves[0])

            if 0 <= row < len(usedMoves) and 0 <= col < len(usedMoves[0]):
                if usedMoves[row][col] == 0:
                    print("O makes a move to square " + str(userMove))
                    usedMoves[row][col] = 2
                    printBoard()
                    break
                else:
                    print("Already taken.")
            else:
                print("Out of range!")

        except ValueError:
            print("Not a number!")


#Main Game
def game():
    #TODO fix end game when board is filled
    while not all(value == 1 or value == 2 for row in usedMoves for value in row):
        userBoardSelection()
        botBoardSelection()

    print("Game ended in a draw!")

#Row Check
def rowCheck():
    for row in usedMoves:
        if not all(value == 1 or value == 2 for value in row):
            return False
    return True
#Col Check
def colCheck():
    for col in range(len(usedMoves[0])):
        values = [row[col] for row in usedMoves]
        if all(value == 1 or value == 2 for value in values):
            continue
        else:
            return False
    return True

#Diag Check

#TODO fix winnerCheck and its sub functions
#Winning check
def winnerCheck():
    if rowCheck():
        print("Winner with rows!")
    if colCheck():
        print("Winner with cols!")



##Start of game

#Clear current screen (Just for testing)
os.system('cls')

#Short 3 line description of program
print("Welcome to Tic-Tac-Toe!\nThis Program was made for the class CAP4630 Intro to AI\nThe purpose of this program is to demonstrate a simple AI that can play the game Tic-Tac-Toe.\n")
selectionBoard()
game()