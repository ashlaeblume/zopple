import z0p
# 3. walk the players
# 4. update array with new player positions
# 5. case where a new player is added to players list
# 6. case where new player is added directly to array
# 7. case where walk destination is out of bounds
# 8. case where walk destination will be occupied by another player: rep/attr?


# moving through a 2D array
# potential problems:
# 2 nodes trying to access same space
# walking out of bounds of board
# wrapping around the list: defining boundaries

# left = cell[i-1]
# middle = cell[i]
# right = cell[i+1]
# up = cell[j-1]
# middle = cell[j]
# down = cell[j+1]

def boardWalk(agent):
    if z0p.GameBoard.pboard[agent.x][agent.y] is None:
        while abs(agent.x) < z0p.GameBoard.size - 1:
            while abs(agent.y) < z0p.GameBoard.size - 2:
                agent.x = agent.x + 1
                agent.y = agent.y + 2
                z0p.GameBoard.pboard[agent.x][agent.y] = agent
            else:
                print("agent.y out of bounds")
        else:
            print("agent.x out of bounds")
    else:
        print("pboard[agent.x][agent.y] already occupied")


z0p.GameBoard.boardWalk(z0p.instances.p0)
