import numpy as np
import random


def random_walk(n):
    position = 0
    walk = [position]
    for i in range(n):
        position += 2*random.randint(0, 1)-1
        walk.append(position)
    return walk


walk = random_walk(35)
walkarray = np.asarray(walk)
walkarray.shape = (6, 6)
walkarray


class RandomWalker:
    def __init__(self):
        self.position = 0

    def walk(self, n):
        self.position = 0
        for i in range(n):
            yield self.position
            self.position += 2*random.randint(0, 1) - 1


walker = RandomWalker()
walk = [position for position in walker.walk(36)]
walkarray = np.asarray(walk)
walkarray.shape = (6, 6)
