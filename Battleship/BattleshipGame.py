# v 0.1  d 9/28/17
# TODO
import Board
import Ship


class BattleshipGame:
    def __init__(self):
        self.board = Board.Board(12, 12)
        for i in range(12):
            for j in range(12):
                self.board.shipLayerP1[i][j] = Ship.Water(j, i)
                self.board.shipLayerP2[i][j] = Ship.Water(j, i)
        self.board.shotLayerP1[:][:] = 'FILLER'
        self.board.shotLayerP2[:][:] = 'FILLER'

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
            print(self.board.shipLayerP1[y][x])
            if self.board.shipType(x, y, receivingPlayer) == 'Water':
                self.board.shotLayerP1[y][x] = False
                return False
            else:
                print(self.board.shipLayerP1[y][x])
                self.board.shotLayerP1[y][x] = True
                print(self.board.shipLayerP1[y][x])
                hitIndex = self.board.shipLayerP1[y][x].getIndex(x, y)
                self.board.shipLayerP1[y][x].hit(hitIndex)
                return True
        if receivingPlayer == 2:
            if self.board.shipType(x, y, receivingPlayer) == 'Water':
                self.board.shotLayerP2[y][x] = False
                return False
            else:
                self.board.shotLayerP2[y][x] = True
                hitIndex = self.board.shipLayerP2[y][x].getIndex(x, y)
                self.board.shipLayerP2[y][x].hit(hitIndex)
                return True

Game = BattleshipGame()
Game.placeShip(1, Ship.Battleship(2, 5, 1))
for y in Game.board.shipLayerP1:
    print(y)
Game.makeGuess(4, 5, 1)
for y in Game.board.shotLayerP1:
    print(y)
