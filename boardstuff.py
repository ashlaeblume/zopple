import random
from gameplayer import gamePlayer
"""
 0.2 Create board
    #b. create players
    #b. add players into players list
    #c. generate players directly into list
    #d. create groupings of players so we can change their laws of motion
"""


class GameBoard():

    def __init__(self, m):
        n = m
        self.size = m
        self.allplayers = []
        # Matrix for storing...what? Player obj with all values embedded?
        self.pboard = [[None for j in range(n)] for i in range(m)]
        # Matrix for storing player locations
        self.plocation = [[None for j in range(n)] for i in range(m)]
        # Matrix for storing frequency states
        self.pfrequency = [[None for j in range(n)] for i in range(m)]
        # Matrix for storing phase states
        self.pphase = [[None for j in range(n)] for i in range(m)]

    def isGamePlayer(thisobj):
        if type(thisobj) is gamePlayer:
            return True

    def isListOfPlayers(playerlist):
        for item in playerlist:
            if all(isinstance(item, gamePlayer)):
                return True

    def addToPlayerList(self, thing):
        if GameBoard.isGamePlayer(thing):
            self.allplayers.append(thing)
        elif GameBoard.isListOfPlayers(thing):
            self.allplayers.extend(thing)

    def isInBoard(self, thing):
        if thing in self.pboard:
            return True
        else:
            return False

    def addToBoard(self, thing):
        if GameBoard.isGamePlayer(thing):
            self.pboard[thing.x][thing.y] == thing
        elif GameBoard.isListOfPlayers(thing):
            for item in thing:
                self.pboard[item.x][item.y] == item

    def addToPosition(self, thing):
        if GameBoard.isGamePlayer(thing):
            self.plocation[thing.x][thing.y] == thing.position
        elif GameBoard.isListOfPlayers(thing):
            for item in thing:
                self.plocation[item.x][item.y] == item.position

    def addToFreqs(self, thing):
        if GameBoard.isGamePlayer(thing):
            self.pfrequency[thing.x][thing.y] == thing.freq
        elif GameBoard.isListOfPlayers(thing):
            for item in thing:
                self.pfrequency[item.x][item.y] == item.freq

    def addToPhases(self, thing):
        if GameBoard.isGamePlayer(thing):
            self.pphase[thing.x][thing.y] == thing.theta
        elif GameBoard.isListOfPlayers(thing):
            for item in thing:
                self.pphase[item.x][item.y] == item.theta

    def generateRandomPlayer(self):
        x0 = random.randint(0, GameBoard.size)
        y0 = random.randint(0, GameBoard.size)
        freq = 6000 * random.random()
        theta = 360 * random.random()
        self.player = gamePlayer(x0, y0, freq, theta)
        return self.player

    def implementNewPlayer(self):
        x0 = random.randint(0, GameBoard.size)
        y0 = random.randint(0,  GameBoard.size)
        if self.pboard[x0][y0] is None:
            self.pboard[x0][y0] == GameBoard.generateRandomPlayer()
        elif self.pboard[x0][y0] is not None:
            x0 = random.randint(0, GameBoard.size)
            y0 = random.randint(0, GameBoard.size)
