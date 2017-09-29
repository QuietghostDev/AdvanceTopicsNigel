# v 0.1  d 9/28/17
# TODO Write getShip function that returns ship

import Ship
import Board


class BattleshipGame:
    def __init__(self):
        self.newBoard = Board(12, 12)

    def placeShip(self, player, ship):
        if ship.orientation == 0:  # Vertical
            for i in range(ship.size):
                if player == 1:
                    self.newBoard.shipLayerP1[ship.y+i][ship.x] = ship.getType()
                if player == 2:
                    self.newBoard.shipLayerP2[ship.y+i][ship.x] = ship.getType()
        if ship.orientation == 1:  # Horizontal
            for i in range(ship.size):
                if player == 1:
                    self.newBoard.shipLayerP1[ship.y][ship.x+i] = ship.getType()
                if player == 2:
                    self.newBoard.shipLayerP2[ship.y][ship.x+i] = ship.getType()

    def getShip(self, shipType):
        pass

    def makeGuess(self, x, y, receivingPlayer):
        if receivingPlayer == 1:
            if self.newBoard.shipType(x, y, receivingPlayer) == 'Water':
                self.newBoard.shotLayerP1[y][x] = False
                return False
            else:
                self.newBoard.shotLayerP1[y][x] = True
                return True
        if receivingPlayer == 2:
            if self.newBoard.shipType(x, y, receivingPlayer) == 'Water':
                self.newBoard.shotLayerP2[y][x] = False
                return False
            else:
                self.newBoard.shotLayerP2[y][x] = True
                return True
