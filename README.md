# Tic-Tac-Toe-using-Minmax

## Introduction
The purpose of this python program was to produce a functional AI that can compete against other AI of its complexity, random movement AI, and human players. The game allows a human to play against the AI on a 3 x 3 grid and place either X’s or O’s to compete in Tic-Tac-Toe. The program follows the rules of Tic-Tac-Toe by tracking each players moves and determines when the game has a winner or ends in a draw.

## Functions
Following along with the python code top to bottom it consists of the following functions and their uses:

1. **printGrid**: Prints the current board with the filled in slots of player moves and if given the input of true it will print out the selection board which consists of a grid 0 to 8 to show the human player where to put their marker (X or O.)
2. **playerCurrentMove**: Checks during the current players move if the selected slot they chose is empty or filled, based on that it will either set a marker or have the user redo selection. During the marker setting it also checks if during the current players turn if they have won the game.
3. **foundWinner**: during the playerCurrentMove winning check this function is called to return a true or false depending on the Tic-Tac-Toe game rules. The winning conditions are if all markers are lined up horizontally, vertically, or diagonally. The latter is checked with the method diagonalWinCheck.
4. **diagonalWinCheck**: called in foundWinner and is used to check from top left of the grid to the bottom right and top right to the bottom left and sees if all the slots diagonally are the same marker.
5. **doesGridHaveEmptySlots**: checks if the game grid has any empty slots
6. **numberOfEmptySlots**: returns the number of empty slots on the grid
7. **availibleSlots**: returns the number of slots that are not taken on the grid
8. **announceMoveAndSwitchPlayers**: after the end of all players turn it announces who move to what slot on the grid, announces the winner of the game (if applicable) and switches whose turn it is once the previous players turn ends.
9. **playGame**: starts the game of Tic Tac Toe, executes printGrid, assigns what player goes first, and loops through the game checking if either the grid no longer has empty slots or if there is a winner announced. If the former, it then announces the game ends in a tie.
10. **getMove**: depending on which class is calling the function it will either place a marker where the human player chooses, randomly places a marker in available slots, or using the minMax function it simulates future moves and chooses the best one.
11. **validMove**: checks if the human player picks a valid slot or if the input is even in the range of 0 to 8.
12. **minMax**: Based on Kylie Ying’s Tic Tac Toe AI, it assigns the AI player as the current maxPlayer, checks if the game has ended first as the function can be called recursively and assigns a score of positive or negative based on the winner, if the grid is filled by this point assigns a score of 0. After which if the current maxPlayer is the AI it assigns a score of negative infinity or positive infinity if the AI is not the maxPlayer.
13. **simulateMoves**: for moves left in the grid the function will check if the slot if taken and if not, it will simulate future moves and compare each with the minMax method by comparing scores. Once all moves are simulated the best one is picked and chosen for the AI current move.
