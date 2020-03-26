import numpy as np

"""
Example from ipython cookbook:
"12.2. Simulating an elementary cellular automaton"
https://ipython-books.github.io/122-simulating-an-elementary-cellular-automaton/
"""


u = np.array[[4], [2], [1]]


def step(x, rule_b):
    # y is a column which contains left,center,right
    # (neighbors?) of each "node"/cell
    # Right value,  #center value x=self,  #left value
    y = np.vstack((np.roll(x, 1), x, np.roll(x, -1))).astype(np.int8)
    return y


"""
# My weird definitions and math formalism stuff
automatum = (Z, S, N, f)
Z = lattice
S = state
N = neighborhood
f = transittion function

thiscell = (position, value)

futime = t+1
pastime = t-1
"""
