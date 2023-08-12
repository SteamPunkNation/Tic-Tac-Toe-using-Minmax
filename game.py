import math
import random
import time

# Andrew Donate
# 6/4/2023 to 6/6/2023
# Project 1


# =#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# The section for the logic of the game
class TicTacToeGame():
    def __init__(self):
        self.grid = [' ' for _ in range(9)]
        self.currentWinner = None

    # The section for the grid of the game
    def printGrid(game, selectionGrid=False):
        if selectionGrid:
            number_grid = [[str(i) for i in range(j*3, (j+1)*3)]
                           for j in range(3)]
            for row in number_grid:
                print('| ' + ' | '.join(row) + ' |')
        else:
            for row in [game.grid[i*3:(i+1) * 3] for i in range(3)]:
                print('| ' + ' | '.join(row) + ' |')

    # Interaction logic
    def playerCurrentMove(game, slot, currentPlayer):
        if game.grid[slot] == ' ':
            game.grid[slot] = currentPlayer
            if game.foundWinner(slot, currentPlayer):
                game.currentWinner = currentPlayer
            return True
        return False

    # Find winner logic
    def foundWinner(game, slot, currentPlayer):
        rowDivder = math.floor(slot / 3)
        currentRow = game.grid[rowDivder * 3: (rowDivder + 1) * 3]

        # Checks if all symbols horizontally match the current player and slot
        if all([symbol == currentPlayer for symbol in currentRow]):
            return True

        colDivder = slot % 3
        currentCol = [game.grid[colDivder + i * 3] for i in range(3)]

        # Checks if all symbols verticallly match the current player and slot
        if all([symbol == currentPlayer for symbol in currentCol]):
            return True

        # Checks if all symbols diagonally match the current player and slot
        if game.diagonalWinCheck(currentPlayer, slot):
            return True

        return False

    # Diagonal winner checker
    @staticmethod
    def diagonalWinCheck(currentPlayer, slot):
        if slot % 2 == 0:
            topLeftToBottomRight = [game.grid[i] for i in [0, 4, 8]]

            if all([symbol == currentPlayer for symbol in topLeftToBottomRight]):
                return True

            topRightToBottomLeft = [game.grid[i] for i in [2, 4, 6]]

            if all([symbol == currentPlayer for symbol in topRightToBottomLeft]):
                return True

        return False

    # Checks if all slots are filled on the board
    def doesGridHaveEmptySlots(game):
        return ' ' in game.grid

    def numberOfEmptySlots(game):
        return game.grid.count(' ')

    def availibleSlots(game):
        return [i for i, x in enumerate(game.grid) if x == ' ']


def announceMoveAndSwitchPlayers(game, currentPlayer, slot):
    # Announces what move the current player has made
    print(currentPlayer + ' makes a move to square {}'.format(slot))
    game.printGrid()
    print('')

    # Announces the game winner (if game is visible)
    if game.currentWinner:
        print(currentPlayer + ' is the winnner!')
        return currentPlayer

    # Switch current player
    currentPlayer = 'O' if currentPlayer == 'X' else 'X'
    return currentPlayer


# The actual gameplay
def playGame(game, playerX, playerO):
    # Print's selection grid
    game.printGrid(True)

    # Assigns the first player of the game
    currentPlayer = 'X'

    while game.doesGridHaveEmptySlots() and game.currentWinner == None:
        if currentPlayer == 'X':
            slot = playerX.getMove(game)
        else:
            slot = playerO.getMove(game)

        if game.playerCurrentMove(slot, currentPlayer):
            currentPlayer = announceMoveAndSwitchPlayers(
                game, currentPlayer, slot)

    if game.currentWinner == None:
        print('Game has ended in a Tie!')


# =#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Player class
class CurrentPlayer():
    def __init__(currentPlayer, symbol):
        currentPlayer.symbol = symbol

    def getMove(currentPlayer, game):
        pass


# =#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# The section for user (Human) interaction
class HumanPlayer(CurrentPlayer):
    def __init__(currentPlayer, symbol):
        super().__init__(symbol)

    def validMove(currentPlayer, slot, game):
        try:
            humanInput = int(slot)
            if humanInput not in game.availibleSlots():
                raise ValueError
            return True
        except ValueError:
            print('Invalid slot. Try again.')
            return False

    def getMove(currentPlayer, game):
        while True:
            slot = input(currentPlayer.symbol + "'s turn. Input move (0-8): ")
            if currentPlayer.validMove(slot, game):
                return int(slot)


# =#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# Computer picks random slots that are not already taken
# Mainly used for testing if the game works at all
class RandomPlayer(CurrentPlayer):
    def __init__(currentPlayer, symbol):
        super().__init__(symbol)

    def getMove(currentPlayer, game):
        return random.choice(game.availibleSlots())


# =#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# The section for the (smart) computer to play
class AiPlayer(CurrentPlayer):
    def __init__(computer, symbol):
        super().__init__(symbol)

    def getMove(currentPlayer, game):
        # If smart bot goes first then just pick randomly
        if len(game.availibleSlots()) == 9:
            return random.choice(game.availibleSlots())
        else:
            time.sleep(1)
            return currentPlayer.minMax(game, currentPlayer.symbol)['position']

    def minMax(self, state, player):
        maxPlayer = self.symbol
        otherPlayer = 'O' if player == 'X' else 'X'

        if state.currentWinner == otherPlayer:
            return {'position': None,
                    'score': 1 * (state.numberOfEmptySlots() + 1)
                    if otherPlayer == maxPlayer
                    else -1 * (state.numberOfEmptySlots() + 1)
                    }
        elif not state.doesGridHaveEmptySlots():
            return {'position': None, 'score': 0}

        if player == maxPlayer:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        return self.simulateMoves(state, player, otherPlayer, maxPlayer, best)

    def simulateMoves(self, state, player, otherPlayer, maxPlayer, best):
        for possibleMove in state.availibleSlots():
            state.playerCurrentMove(possibleMove, player)
            simulatedScore = self.minMax(state, otherPlayer)

            state.grid[possibleMove] = ' '
            state.currentWinner = None
            simulatedScore['position'] = possibleMove

            if player == maxPlayer:
                if simulatedScore['score'] > best['score']:
                    best = simulatedScore
            else:
                if simulatedScore['score'] < best['score']:
                    best = simulatedScore

        return best


# =#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
# The "main function" of this python file
if __name__ == '__main__':
    print("Welcome to Tic-Tac-Toe!\nThis Program was made for the class CAP4630 Intro to AI\nThe purpose of this program is to demonstrate a simple AI that can play the game Tic-Tac-Toe.\n")
    while True:
        playerX = HumanPlayer('X')
        playerO = AiPlayer('O')
        game = TicTacToeGame()
        playGame(game, playerX, playerO)
        playAgain = input('Play again? (y/n): ')
        if playAgain.lower() != 'y':
            break
