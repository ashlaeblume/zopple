#!/usr/bin/env python
# coding: utf-8

# In[84]:


# Toroidal Edge version of game of life
# such that each node in the 2D list includes its neighbors
# "off the edge" of the array, e.g., index values wrap around the list

import random
import numpy as np

#test values
#m,n=6,6
m = int(input("enter desired board length:"))
n = m
print(m)

randboard = [[random.randint(0,1) for j in range(n)] for i in range (m)]

empty2Dlist = [[None for p in range(n)] for q in range (m)]

nxt = empty2Dlist

board = randboard

# Checking a small neighborhood of distance |1| around the every node in the board
for i in range(m):  #[i,j] is the center of the nbhd
    for j in range(n):
        neighbortot = 0
        neighborlist = []
        print("now checking neighbors of",i,j)
        for k in range((i-1),(i+2)):  #k,l generates the window around node [i,j]
            for l in range((j-1),(j+2)):
                thisneighbor = board[k%m][l%n]
                neighborlist.append(neighbors)
                print('neighbors at node',k%m,l%n,"=", thisneighbor)
                neighbortot = neighbortot + thisneighbor
        realtotal = neighbortot - 1
        print("neighbor TOTAL of",i,j,"is",realtotal)
# Rules of Life
        if (board[i][j] == 1) & (realtotal < 2):
            nxt[i][j]=0
        elif (board[i][j] == 1) & (realtotal > 3):
            nxt[i][j]=0
        elif (board[i][j] == 0) & (realtotal == 3):
            nxt[i][j]=1
        else:
            nxt[i][j] = board[i][j]
            
#print arrays so we can check values
for q in board:
    print(*q)

print('\n')

for q in nxt:
    print(*q)


# In[86]:


# Created by ashlaeblume, February 2020
# Toroidal Edge version of Conway's Game of Life
# Each node is looking at a window of neighbors which is a distance of |1| away from itself
# It counts its nearest neighbors and applies the Rules of Life to determine next board state

import random
import numpy as np

m = int(input("enter desired board length:"))
n = m
print(m)

# Initializing boards
randboard = [[random.randint(0,1) for j in range(n)] for i in range (m)]
empty2Dlist = [[None for p in range(n)] for q in range (m)]
nxt = empty2Dlist
board = randboard

# Checking a small neighborhood of distance |1| around the every node in the board
for i in range(m):  #[i,j] is the center of the nbhd
    for j in range(n):
        neighbortot = 0
        neighborlist = []
        print("now checking neighbors of",i,j)
        for k in range((i-1),(i+2)):  #k,l generates the window around node [i,j]
            for l in range((j-1),(j+2)):
                thisneighbor = board[k%m][l%n]
                neighborlist.append(neighbors)
                neighbortot = neighbortot + thisneighbor
        realtotal = neighbortot - 1
        print("neighbor TOTAL of",i,j,"is",realtotal)
# Rules of Life
        if (board[i][j] == 1) & (realtotal < 2):
            nxt[i][j]=0
        elif (board[i][j] == 1) & (realtotal > 3):
            nxt[i][j]=0
        elif (board[i][j] == 0) & (realtotal == 3):
            nxt[i][j]=1
        else:
            nxt[i][j] = board[i][j]            

# Prints the board and next state so we can check values
for q in board:
    print(*q)

print('\n')

for q in nxt:
    print(*q)


# In[ ]:




