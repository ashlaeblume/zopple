# 0.1 Create players
class gamePlayer():

    def __init__(self, x, y, freq, theta):
        self.x = x
        self.y = y
        self.position = [x, y]
        self.freq = freq
        self.theta = theta
        self.params = [x, y, freq, theta]

    def __repr__(self):
        return ("gamePlayer")


# Bleeps do one thing
class Bleep():


# Bloops do another
class Bloop():
