# v 0.1 Build 001  d 9/29/17
# TODO Make graphics
# TODO Finish functionality
import Board
import Ship


class BattleshipGame:
    def __init__(self):
        self.board = Board.Board(12, 12)
        for i in range(12):
            for j in range(12):
                self.board.shipLayerP1[i][j] = Ship.Water(j, i)
                self.board.shipLayerP2[i][j] = Ship.Water(j, i)

    def placeShip(self, player, ship):
        if ship.orientation == 0:  # Vertical
            for i in range(ship.size):
                if player == 1:
                    self.board.shipLayerP1[ship.y + i][ship.x] = ship
                if player == 2:
                    self.board.shipLayerP2[ship.y + i][ship.x] = ship
        if ship.orientation == 1:  # Horizontal
            for i in range(ship.size):
                if player == 1:
                    self.board.shipLayerP1[ship.y][ship.x + i] = ship
                if player == 2:
                    self.board.shipLayerP2[ship.y][ship.x + i] = ship

    def makeGuess(self, x, y, receivingPlayer):
        if receivingPlayer == 1:
            if self.board.shotLayerP1[y][x] is None:
                guess = self.board.shipLayerP1[y][x]
                if self.board.shipType(x, y, receivingPlayer) == 'Water':
                    self.board.shotLayerP1[y][x] = False
                    return False
                else:
                    self.board.shotLayerP1[y][x] = True
                    hitIndex = guess.getIndex(x, y)
                    guess.hit(hitIndex)
                    return True
            else:
                raise "guess not none"
        if receivingPlayer == 2:
            if self.board.shotLayerP2[y][x] is None:
                guess = self.board.shipLayerP2[y][x]
                if self.board.shipType(x, y, receivingPlayer) == 'Water':
                    self.board.shotLayerP2[y][x] = False
                    return False
                else:
                    self.board.shotLayerP2[y][x] = True
                    hitIndex = guess.getIndex(x, y)
                    guess.hit(hitIndex)
                    return True
