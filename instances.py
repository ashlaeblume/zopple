from player import gamePlayer
from boardstuff import GameBoard

m, n = 5, 5
b = GameBoard(5)

p0 = gamePlayer(2, 3, 660, 90)
p1 = gamePlayer(3, 0, 440, 0)
p2 = gamePlayer(1, 1, 220, 45)
p3 = gamePlayer(2, 1, 880, 180)
p4 = gamePlayer(0, 0, 345, 67)
p5 = gamePlayer(4, 2, 880, 122)
playerlist = [p0, p1, p2]

b.isGamePlayer(p0)
b.isListOfPlayers(playerlist)
b.addToPlayerList(p4)
b.isInBoard(p2)
b.addToBoard(p5)
b.addToPosition(p5)
b.addToFreqs(p5)
b.addToPhase(p5)
b.generateRandomPlayer()
b.implementNewPlayer()

p6 = GameBoard.generatePlayer()
GameBoard.generateRandomPlayer(p4)
p7 = GameBoard.generateRandomPlayer()
GameBoard.returnPlayerVals(p2)
b.generateRandomPlayer()
